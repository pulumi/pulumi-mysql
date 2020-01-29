// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package mysql

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The ``.Database`` resource creates and manages a database on a MySQL
// server.
// 
// > **Caution:** The ``.Database`` resource can completely delete your
// database just as easily as it can create it. To avoid costly accidents,
// consider setting
// [``preventDestroy``](https://www.terraform.io/docs/configuration/resources.html#prevent_destroy)
// on your database resources as an extra safety measure.
// 
// > This content is derived from https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/database.html.markdown.
type Database struct {
	pulumi.CustomResourceState

	// The default character set to use when
	// a table is created without specifying an explicit character set. Defaults
	// to "utf8".
	DefaultCharacterSet pulumi.StringPtrOutput `pulumi:"defaultCharacterSet"`
	// The default collation to use when a table
	// is created without specifying an explicit collation. Defaults to
	// ``utf8GeneralCi``. Each character set has its own set of collations, so
	// changing the character set requires also changing the collation.
	DefaultCollation pulumi.StringPtrOutput `pulumi:"defaultCollation"`
	// The name of the database. This must be unique within
	// a given MySQL server and may or may not be case-sensitive depending on
	// the operating system on which the MySQL server is running.
	Name pulumi.StringOutput `pulumi:"name"`
}

// NewDatabase registers a new resource with the given unique name, arguments, and options.
func NewDatabase(ctx *pulumi.Context,
	name string, args *DatabaseArgs, opts ...pulumi.ResourceOption) (*Database, error) {
	if args == nil {
		args = &DatabaseArgs{}
	}
	var resource Database
	err := ctx.RegisterResource("mysql:index/database:Database", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDatabase gets an existing Database resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatabase(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DatabaseState, opts ...pulumi.ResourceOption) (*Database, error) {
	var resource Database
	err := ctx.ReadResource("mysql:index/database:Database", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Database resources.
type databaseState struct {
	// The default character set to use when
	// a table is created without specifying an explicit character set. Defaults
	// to "utf8".
	DefaultCharacterSet *string `pulumi:"defaultCharacterSet"`
	// The default collation to use when a table
	// is created without specifying an explicit collation. Defaults to
	// ``utf8GeneralCi``. Each character set has its own set of collations, so
	// changing the character set requires also changing the collation.
	DefaultCollation *string `pulumi:"defaultCollation"`
	// The name of the database. This must be unique within
	// a given MySQL server and may or may not be case-sensitive depending on
	// the operating system on which the MySQL server is running.
	Name *string `pulumi:"name"`
}

type DatabaseState struct {
	// The default character set to use when
	// a table is created without specifying an explicit character set. Defaults
	// to "utf8".
	DefaultCharacterSet pulumi.StringPtrInput
	// The default collation to use when a table
	// is created without specifying an explicit collation. Defaults to
	// ``utf8GeneralCi``. Each character set has its own set of collations, so
	// changing the character set requires also changing the collation.
	DefaultCollation pulumi.StringPtrInput
	// The name of the database. This must be unique within
	// a given MySQL server and may or may not be case-sensitive depending on
	// the operating system on which the MySQL server is running.
	Name pulumi.StringPtrInput
}

func (DatabaseState) ElementType() reflect.Type {
	return reflect.TypeOf((*databaseState)(nil)).Elem()
}

type databaseArgs struct {
	// The default character set to use when
	// a table is created without specifying an explicit character set. Defaults
	// to "utf8".
	DefaultCharacterSet *string `pulumi:"defaultCharacterSet"`
	// The default collation to use when a table
	// is created without specifying an explicit collation. Defaults to
	// ``utf8GeneralCi``. Each character set has its own set of collations, so
	// changing the character set requires also changing the collation.
	DefaultCollation *string `pulumi:"defaultCollation"`
	// The name of the database. This must be unique within
	// a given MySQL server and may or may not be case-sensitive depending on
	// the operating system on which the MySQL server is running.
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a Database resource.
type DatabaseArgs struct {
	// The default character set to use when
	// a table is created without specifying an explicit character set. Defaults
	// to "utf8".
	DefaultCharacterSet pulumi.StringPtrInput
	// The default collation to use when a table
	// is created without specifying an explicit collation. Defaults to
	// ``utf8GeneralCi``. Each character set has its own set of collations, so
	// changing the character set requires also changing the collation.
	DefaultCollation pulumi.StringPtrInput
	// The name of the database. This must be unique within
	// a given MySQL server and may or may not be case-sensitive depending on
	// the operating system on which the MySQL server is running.
	Name pulumi.StringPtrInput
}

func (DatabaseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*databaseArgs)(nil)).Elem()
}

