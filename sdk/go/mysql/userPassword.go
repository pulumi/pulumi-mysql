// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mysql

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// > This content is derived from https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/user_password.html.markdown.
type UserPassword struct {
	s *pulumi.ResourceState
}

// NewUserPassword registers a new resource with the given unique name, arguments, and options.
func NewUserPassword(ctx *pulumi.Context,
	name string, args *UserPasswordArgs, opts ...pulumi.ResourceOpt) (*UserPassword, error) {
	if args == nil || args.PgpKey == nil {
		return nil, errors.New("missing required argument 'PgpKey'")
	}
	if args == nil || args.User == nil {
		return nil, errors.New("missing required argument 'User'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["host"] = nil
		inputs["pgpKey"] = nil
		inputs["user"] = nil
	} else {
		inputs["host"] = args.Host
		inputs["pgpKey"] = args.PgpKey
		inputs["user"] = args.User
	}
	inputs["encryptedPassword"] = nil
	inputs["keyFingerprint"] = nil
	s, err := ctx.RegisterResource("mysql:index/userPassword:UserPassword", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &UserPassword{s: s}, nil
}

// GetUserPassword gets an existing UserPassword resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetUserPassword(ctx *pulumi.Context,
	name string, id pulumi.ID, state *UserPasswordState, opts ...pulumi.ResourceOpt) (*UserPassword, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["encryptedPassword"] = state.EncryptedPassword
		inputs["host"] = state.Host
		inputs["keyFingerprint"] = state.KeyFingerprint
		inputs["pgpKey"] = state.PgpKey
		inputs["user"] = state.User
	}
	s, err := ctx.ReadResource("mysql:index/userPassword:UserPassword", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &UserPassword{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *UserPassword) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *UserPassword) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The encrypted password, base64 encoded.
func (r *UserPassword) EncryptedPassword() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["encryptedPassword"])
}

// The source host of the user. Defaults to `localhost`.
func (r *UserPassword) Host() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["host"])
}

// The fingerprint of the PGP key used to encrypt the password 
func (r *UserPassword) KeyFingerprint() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["keyFingerprint"])
}

// Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
func (r *UserPassword) PgpKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["pgpKey"])
}

// The IAM user to associate with this access key.
func (r *UserPassword) User() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["user"])
}

// Input properties used for looking up and filtering UserPassword resources.
type UserPasswordState struct {
	// The encrypted password, base64 encoded.
	EncryptedPassword interface{}
	// The source host of the user. Defaults to `localhost`.
	Host interface{}
	// The fingerprint of the PGP key used to encrypt the password 
	KeyFingerprint interface{}
	// Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
	PgpKey interface{}
	// The IAM user to associate with this access key.
	User interface{}
}

// The set of arguments for constructing a UserPassword resource.
type UserPasswordArgs struct {
	// The source host of the user. Defaults to `localhost`.
	Host interface{}
	// Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
	PgpKey interface{}
	// The IAM user to associate with this access key.
	User interface{}
}
