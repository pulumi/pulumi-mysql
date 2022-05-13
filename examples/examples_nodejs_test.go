// Copyright 2016-2017, Pulumi Corporation.  All rights reserved.
//go:build nodejs || all
// +build nodejs all

package examples

import (
	"path"
	"testing"

	"github.com/pulumi/pulumi/pkg/v3/testing/integration"
)

func TestAccDatabase(t *testing.T) {
	test := getJSBaseOptions(t).
		With(integration.ProgramTestOptions{
			Dir: path.Join(getCwd(t), "database"),
			// The default character set for the MySQL Docker image has diverged from the upstream provider's value.
			// Since the upstream provider has been archived and will not be updated, we'll simply expect changes after
			// creating a DB with the default options:
			AllowEmptyPreviewChanges: true,
			AllowEmptyUpdateChanges:  true,
			ExpectRefreshChanges:     true,
		})

	integration.ProgramTest(t, &test)
}

func getJSBaseOptions(t *testing.T) integration.ProgramTestOptions {
	base := getBaseOptions()
	baseJS := base.With(integration.ProgramTestOptions{
		Dependencies: []string{
			"@pulumi/mysql",
		},
	})

	return baseJS
}
