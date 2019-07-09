// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mysql

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// The ``mysql_user`` resource creates and manages a user on a MySQL
// server.
// 
// > **Note:** The password for the user is provided in plain text, and is
// obscured by an unsalted hash in the state
// [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
// Care is required when using this resource, to avoid disclosing the password.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/user.html.markdown.
type User struct {
	s *pulumi.ResourceState
}

// NewUser registers a new resource with the given unique name, arguments, and options.
func NewUser(ctx *pulumi.Context,
	name string, args *UserArgs, opts ...pulumi.ResourceOpt) (*User, error) {
	if args == nil || args.User == nil {
		return nil, errors.New("missing required argument 'User'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["authPlugin"] = nil
		inputs["host"] = nil
		inputs["password"] = nil
		inputs["plaintextPassword"] = nil
		inputs["tlsOption"] = nil
		inputs["user"] = nil
	} else {
		inputs["authPlugin"] = args.AuthPlugin
		inputs["host"] = args.Host
		inputs["password"] = args.Password
		inputs["plaintextPassword"] = args.PlaintextPassword
		inputs["tlsOption"] = args.TlsOption
		inputs["user"] = args.User
	}
	s, err := ctx.RegisterResource("mysql:index/user:User", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &User{s: s}, nil
}

// GetUser gets an existing User resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUser(ctx *pulumi.Context,
	name string, id pulumi.ID, state *UserState, opts ...pulumi.ResourceOpt) (*User, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["authPlugin"] = state.AuthPlugin
		inputs["host"] = state.Host
		inputs["password"] = state.Password
		inputs["plaintextPassword"] = state.PlaintextPassword
		inputs["tlsOption"] = state.TlsOption
		inputs["user"] = state.User
	}
	s, err := ctx.ReadResource("mysql:index/user:User", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &User{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *User) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *User) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintext_password`.  
func (r *User) AuthPlugin() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["authPlugin"])
}

// The source host of the user. Defaults to "localhost".
func (r *User) Host() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["host"])
}

// Deprecated alias of `plaintext_password`, whose value is *stored as plaintext in state*. Prefer to use `plaintext_password` instead, which stores the password as an unsalted hash. Conflicts with `auth_plugin`.
func (r *User) Password() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["password"])
}

// The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `auth_plugin`.
func (r *User) PlaintextPassword() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["plaintextPassword"])
}

// An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
func (r *User) TlsOption() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["tlsOption"])
}

// The name of the user.
func (r *User) User() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["user"])
}

// Input properties used for looking up and filtering User resources.
type UserState struct {
	// Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintext_password`.  
	AuthPlugin interface{}
	// The source host of the user. Defaults to "localhost".
	Host interface{}
	// Deprecated alias of `plaintext_password`, whose value is *stored as plaintext in state*. Prefer to use `plaintext_password` instead, which stores the password as an unsalted hash. Conflicts with `auth_plugin`.
	Password interface{}
	// The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `auth_plugin`.
	PlaintextPassword interface{}
	// An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
	TlsOption interface{}
	// The name of the user.
	User interface{}
}

// The set of arguments for constructing a User resource.
type UserArgs struct {
	// Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintext_password`.  
	AuthPlugin interface{}
	// The source host of the user. Defaults to "localhost".
	Host interface{}
	// Deprecated alias of `plaintext_password`, whose value is *stored as plaintext in state*. Prefer to use `plaintext_password` instead, which stores the password as an unsalted hash. Conflicts with `auth_plugin`.
	Password interface{}
	// The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `auth_plugin`.
	PlaintextPassword interface{}
	// An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
	TlsOption interface{}
	// The name of the user.
	User interface{}
}
