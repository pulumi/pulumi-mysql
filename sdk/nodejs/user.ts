// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The ``mysql.User`` resource creates and manages a user on a MySQL
 * server.
 *
 * ## Examples
 *
 * ### Basic Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mysql from "@pulumi/mysql";
 *
 * const jdoe = new mysql.User("jdoe", {
 *     host: "example.com",
 *     plaintextPassword: "password",
 *     user: "jdoe",
 * });
 * ```
 *
 * ### Example Usage with an Authentication Plugin
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mysql from "@pulumi/mysql";
 *
 * const nologin = new mysql.User("nologin", {
 *     authPlugin: "mysql_no_login",
 *     host: "example.com",
 *     user: "nologin",
 * });
 * ```
 */
export class User extends pulumi.CustomResource {
    /**
     * Get an existing User resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserState, opts?: pulumi.CustomResourceOptions): User {
        return new User(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'mysql:index/user:User';

    /**
     * Returns true if the given object is an instance of User.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is User {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === User.__pulumiType;
    }

    /**
     * Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintextPassword`.
     */
    public readonly authPlugin!: pulumi.Output<string | undefined>;
    /**
     * The source host of the user. Defaults to "localhost".
     */
    public readonly host!: pulumi.Output<string | undefined>;
    /**
     * Deprecated alias of `plaintextPassword`, whose value is *stored as plaintext in state*. Prefer to use `plaintextPassword` instead, which stores the password as an unsalted hash. Conflicts with `authPlugin`.
     *
     * @deprecated Please use plaintext_password instead
     */
    public readonly password!: pulumi.Output<string | undefined>;
    /**
     * The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `authPlugin`.
     */
    public readonly plaintextPassword!: pulumi.Output<string | undefined>;
    /**
     * An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
     */
    public readonly tlsOption!: pulumi.Output<string | undefined>;
    /**
     * The name of the user.
     */
    public readonly user!: pulumi.Output<string>;

    /**
     * Create a User resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: UserArgs | UserState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as UserState | undefined;
            resourceInputs["authPlugin"] = state ? state.authPlugin : undefined;
            resourceInputs["host"] = state ? state.host : undefined;
            resourceInputs["password"] = state ? state.password : undefined;
            resourceInputs["plaintextPassword"] = state ? state.plaintextPassword : undefined;
            resourceInputs["tlsOption"] = state ? state.tlsOption : undefined;
            resourceInputs["user"] = state ? state.user : undefined;
        } else {
            const args = argsOrState as UserArgs | undefined;
            if ((!args || args.user === undefined) && !opts.urn) {
                throw new Error("Missing required property 'user'");
            }
            resourceInputs["authPlugin"] = args ? args.authPlugin : undefined;
            resourceInputs["host"] = args ? args.host : undefined;
            resourceInputs["password"] = args ? args.password : undefined;
            resourceInputs["plaintextPassword"] = args ? args.plaintextPassword : undefined;
            resourceInputs["tlsOption"] = args ? args.tlsOption : undefined;
            resourceInputs["user"] = args ? args.user : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(User.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering User resources.
 */
export interface UserState {
    /**
     * Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintextPassword`.
     */
    authPlugin?: pulumi.Input<string>;
    /**
     * The source host of the user. Defaults to "localhost".
     */
    host?: pulumi.Input<string>;
    /**
     * Deprecated alias of `plaintextPassword`, whose value is *stored as plaintext in state*. Prefer to use `plaintextPassword` instead, which stores the password as an unsalted hash. Conflicts with `authPlugin`.
     *
     * @deprecated Please use plaintext_password instead
     */
    password?: pulumi.Input<string>;
    /**
     * The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `authPlugin`.
     */
    plaintextPassword?: pulumi.Input<string>;
    /**
     * An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
     */
    tlsOption?: pulumi.Input<string>;
    /**
     * The name of the user.
     */
    user?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a User resource.
 */
export interface UserArgs {
    /**
     * Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintextPassword`.
     */
    authPlugin?: pulumi.Input<string>;
    /**
     * The source host of the user. Defaults to "localhost".
     */
    host?: pulumi.Input<string>;
    /**
     * Deprecated alias of `plaintextPassword`, whose value is *stored as plaintext in state*. Prefer to use `plaintextPassword` instead, which stores the password as an unsalted hash. Conflicts with `authPlugin`.
     *
     * @deprecated Please use plaintext_password instead
     */
    password?: pulumi.Input<string>;
    /**
     * The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `authPlugin`.
     */
    plaintextPassword?: pulumi.Input<string>;
    /**
     * An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
     */
    tlsOption?: pulumi.Input<string>;
    /**
     * The name of the user.
     */
    user: pulumi.Input<string>;
}
