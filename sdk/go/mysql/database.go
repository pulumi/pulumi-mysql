// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mysql

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The ``mysql_database`` resource creates and manages a database on a MySQL
// server.
// 
// > **Caution:** The ``mysql_database`` resource can completely delete your
// database just as easily as it can create it. To avoid costly accidents,
// consider setting
// [``prevent_destroy``](https://www.terraform.io/docs/configuration/resources.html#prevent_destroy)
// on your database resources as an extra safety measure.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/database.html.markdown.
type Database struct {
	s *pulumi.ResourceState
}

// NewDatabase registers a new resource with the given unique name, arguments, and options.
func NewDatabase(ctx *pulumi.Context,
	name string, args *DatabaseArgs, opts ...pulumi.ResourceOpt) (*Database, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["defaultCharacterSet"] = nil
		inputs["defaultCollation"] = nil
		inputs["name"] = nil
	} else {
		inputs["defaultCharacterSet"] = args.DefaultCharacterSet
		inputs["defaultCollation"] = args.DefaultCollation
		inputs["name"] = args.Name
	}
	s, err := ctx.RegisterResource("mysql:index/database:Database", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Database{s: s}, nil
}

// GetDatabase gets an existing Database resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatabase(ctx *pulumi.Context,
	name string, id pulumi.ID, state *DatabaseState, opts ...pulumi.ResourceOpt) (*Database, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["defaultCharacterSet"] = state.DefaultCharacterSet
		inputs["defaultCollation"] = state.DefaultCollation
		inputs["name"] = state.Name
	}
	s, err := ctx.ReadResource("mysql:index/database:Database", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Database{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Database) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Database) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The default character set to use when
// a table is created without specifying an explicit character set. Defaults
// to "utf8".
func (r *Database) DefaultCharacterSet() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["defaultCharacterSet"])
}

// The default collation to use when a table
// is created without specifying an explicit collation. Defaults to
// ``utf8_general_ci``. Each character set has its own set of collations, so
// changing the character set requires also changing the collation.
func (r *Database) DefaultCollation() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["defaultCollation"])
}

// The name of the database. This must be unique within
// a given MySQL server and may or may not be case-sensitive depending on
// the operating system on which the MySQL server is running.
func (r *Database) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Input properties used for looking up and filtering Database resources.
type DatabaseState struct {
	// The default character set to use when
	// a table is created without specifying an explicit character set. Defaults
	// to "utf8".
	DefaultCharacterSet interface{}
	// The default collation to use when a table
	// is created without specifying an explicit collation. Defaults to
	// ``utf8_general_ci``. Each character set has its own set of collations, so
	// changing the character set requires also changing the collation.
	DefaultCollation interface{}
	// The name of the database. This must be unique within
	// a given MySQL server and may or may not be case-sensitive depending on
	// the operating system on which the MySQL server is running.
	Name interface{}
}

// The set of arguments for constructing a Database resource.
type DatabaseArgs struct {
	// The default character set to use when
	// a table is created without specifying an explicit character set. Defaults
	// to "utf8".
	DefaultCharacterSet interface{}
	// The default collation to use when a table
	// is created without specifying an explicit collation. Defaults to
	// ``utf8_general_ci``. Each character set has its own set of collations, so
	// changing the character set requires also changing the collation.
	DefaultCollation interface{}
	// The name of the database. This must be unique within
	// a given MySQL server and may or may not be case-sensitive depending on
	// the operating system on which the MySQL server is running.
	Name interface{}
}
