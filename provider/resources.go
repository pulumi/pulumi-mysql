// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package mysql

import (
	"fmt"
	"path"
	// embed is used to store bridge-metadata.json in the compiled binary
	_ "embed"

	"github.com/hashicorp/terraform-plugin-sdk/helper/schema"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge/tokens"
	shimv1 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v1"
	"github.com/terraform-providers/terraform-provider-mysql/mysql"

	"github.com/pulumi/pulumi-mysql/provider/v3/pkg/version"
)

// all of the token components used below.
const (
	// packages:
	mainPkg = "mysql"
	// modules:
	mainMod = "index"
)

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	p := shimv1.NewProvider(mysql.Provider().(*schema.Provider))

	prov := tfbridge.ProviderInfo{
		P:                p,
		Name:             "mysql",
		Description:      "A Pulumi package for creating and managing mysql cloud resources.",
		Keywords:         []string{"pulumi", "mysql"},
		License:          "Apache-2.0",
		Homepage:         "https://pulumi.io",
		Repository:       "https://github.com/pulumi/pulumi-mysql",
		MetadataInfo:     tfbridge.NewProviderMetadata(metadata),
		Version:          version.Version,
		UpstreamRepoPath: "./upstream",

		Config: map[string]*tfbridge.SchemaInfo{
			"proxy": {
				Default: &tfbridge.DefaultInfo{
					EnvVars: []string{"ALL_PROXY", "all_proxy"},
				},
			},
			"tls": {
				Default: &tfbridge.DefaultInfo{
					EnvVars: []string{"MYSQL_TLS_CONFIG"},
					Value:   "false",
				},
			},
		},
		Resources: map[string]*tfbridge.ResourceInfo{
			"mysql_grant": {
				Fields: map[string]*tfbridge.SchemaInfo{
					"grant": {CSharpName: "GrantName"},
				},
			},
			"mysql_user": {
				Fields: map[string]*tfbridge.SchemaInfo{
					"user": {CSharpName: "UserName"},
				},
			},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0-alpha.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
		},
		Python: &tfbridge.PythonInfo{
			Requires: map[string]string{
				"pulumi": ">=3.0.0a1,<4.0.0",
			},
			PyProject: struct{ Enabled bool }{true},
		},

		Golang: &tfbridge.GolangInfo{
			ImportBasePath: path.Join(
				fmt.Sprintf("github.com/pulumi/pulumi-%[1]s/sdk/", mainPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi": "3.*-*",
			},
			Namespaces: map[string]string{
				mainPkg: "MySql",
			},
		},
	}

	prov.MustComputeTokens(tokens.SingleModule("mysql_", mainMod,
		tokens.MakeStandard(mainPkg)))
	prov.MustApplyAutoAliases()
	prov.SetAutonaming(255, "-")

	return prov
}

//go:embed cmd/pulumi-resource-mysql/bridge-metadata.json
var metadata []byte
