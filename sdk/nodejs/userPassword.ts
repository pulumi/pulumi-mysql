// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The `mysql.UserPassword` resource sets and manages a password for a given
 * user on a MySQL server.
 *
 * > **NOTE on MySQL Passwords:** This resource conflicts with the `password`
 *    argument for `mysql.User`. This resource uses PGP encryption to avoid
 *    storing unencrypted passwords in the provider state.
 *
 * > **NOTE on How Passwords are Created:** This resource **automatically**
 *    generates a **random** password. The password will be a random UUID.
 */
export class UserPassword extends pulumi.CustomResource {
    /**
     * Get an existing UserPassword resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserPasswordState, opts?: pulumi.CustomResourceOptions): UserPassword {
        return new UserPassword(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'mysql:index/userPassword:UserPassword';

    /**
     * Returns true if the given object is an instance of UserPassword.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is UserPassword {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === UserPassword.__pulumiType;
    }

    /**
     * The encrypted password, base64 encoded.
     */
    public /*out*/ readonly encryptedPassword!: pulumi.Output<string>;
    /**
     * The source host of the user. Defaults to `localhost`.
     */
    public readonly host!: pulumi.Output<string | undefined>;
    /**
     * The fingerprint of the PGP key used to encrypt the password
     */
    public /*out*/ readonly keyFingerprint!: pulumi.Output<string>;
    /**
     * Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
     */
    public readonly pgpKey!: pulumi.Output<string>;
    /**
     * The IAM user to associate with this access key.
     */
    public readonly user!: pulumi.Output<string>;

    /**
     * Create a UserPassword resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserPasswordArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: UserPasswordArgs | UserPasswordState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as UserPasswordState | undefined;
            inputs["encryptedPassword"] = state ? state.encryptedPassword : undefined;
            inputs["host"] = state ? state.host : undefined;
            inputs["keyFingerprint"] = state ? state.keyFingerprint : undefined;
            inputs["pgpKey"] = state ? state.pgpKey : undefined;
            inputs["user"] = state ? state.user : undefined;
        } else {
            const args = argsOrState as UserPasswordArgs | undefined;
            if ((!args || args.pgpKey === undefined) && !opts.urn) {
                throw new Error("Missing required property 'pgpKey'");
            }
            if ((!args || args.user === undefined) && !opts.urn) {
                throw new Error("Missing required property 'user'");
            }
            inputs["host"] = args ? args.host : undefined;
            inputs["pgpKey"] = args ? args.pgpKey : undefined;
            inputs["user"] = args ? args.user : undefined;
            inputs["encryptedPassword"] = undefined /*out*/;
            inputs["keyFingerprint"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(UserPassword.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering UserPassword resources.
 */
export interface UserPasswordState {
    /**
     * The encrypted password, base64 encoded.
     */
    encryptedPassword?: pulumi.Input<string>;
    /**
     * The source host of the user. Defaults to `localhost`.
     */
    host?: pulumi.Input<string>;
    /**
     * The fingerprint of the PGP key used to encrypt the password
     */
    keyFingerprint?: pulumi.Input<string>;
    /**
     * Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
     */
    pgpKey?: pulumi.Input<string>;
    /**
     * The IAM user to associate with this access key.
     */
    user?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a UserPassword resource.
 */
export interface UserPasswordArgs {
    /**
     * The source host of the user. Defaults to `localhost`.
     */
    host?: pulumi.Input<string>;
    /**
     * Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
     */
    pgpKey: pulumi.Input<string>;
    /**
     * The IAM user to associate with this access key.
     */
    user: pulumi.Input<string>;
}
