// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The ``mysql_grant`` resource creates and manages privileges given to
 * a user on a MySQL server.
 * 
 * ## Granting Privileges to a User
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mysql from "@pulumi/mysql";
 * 
 * const jdoeUser = new mysql.User("jdoe", {
 *     host: "example.com",
 *     password: "password",
 *     user: "jdoe",
 * });
 * const jdoeGrant = new mysql.Grant("jdoe", {
 *     database: "app",
 *     host: jdoeUser.host,
 *     privileges: [
 *         "SELECT",
 *         "UPDATE",
 *     ],
 *     user: jdoeUser.user,
 * });
 * ```
 * 
 * ## Granting Privileges to a Role
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mysql from "@pulumi/mysql";
 * 
 * const developerRole = new mysql.Role("developer", {});
 * const developerGrant = new mysql.Grant("developer", {
 *     database: "app",
 *     privileges: [
 *         "SELECT",
 *         "UPDATE",
 *     ],
 *     role: developerRole.name,
 * });
 * ```
 * 
 * ## Adding a Role to a User
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mysql from "@pulumi/mysql";
 * 
 * const developerRole = new mysql.Role("developer", {});
 * const jdoe = new mysql.User("jdoe", {
 *     host: "example.com",
 *     password: "password",
 *     user: "jdoe",
 * });
 * const developerGrant = new mysql.Grant("developer", {
 *     database: "app",
 *     host: jdoe.host,
 *     roles: [developerRole.name],
 *     user: jdoe.user,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-mysql/blob/master/website/docs/r/grant.html.markdown.
 */
export class Grant extends pulumi.CustomResource {
    /**
     * Get an existing Grant resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GrantState, opts?: pulumi.CustomResourceOptions): Grant {
        return new Grant(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'mysql:index/grant:Grant';

    /**
     * Returns true if the given object is an instance of Grant.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Grant {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Grant.__pulumiType;
    }

    /**
     * The database to grant privileges on.
     */
    public readonly database!: pulumi.Output<string>;
    /**
     * Whether to also give the user privileges to grant the same privileges to other users.
     */
    public readonly grant!: pulumi.Output<boolean | undefined>;
    /**
     * The source host of the user. Defaults to "localhost". Conflicts with `role`.
     */
    public readonly host!: pulumi.Output<string | undefined>;
    /**
     * A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
     */
    public readonly privileges!: pulumi.Output<string[] | undefined>;
    /**
     * The role to grant `privileges` to. Conflicts with `user` and `host`.
     */
    public readonly role!: pulumi.Output<string | undefined>;
    /**
     * A list of rols to grant to the user. Conflicts with `privileges`.
     */
    public readonly roles!: pulumi.Output<string[] | undefined>;
    /**
     * Which table to grant `privileges` on. Defaults to `*`, which is all tables.
     */
    public readonly table!: pulumi.Output<string | undefined>;
    /**
     * An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
     */
    public readonly tlsOption!: pulumi.Output<string | undefined>;
    /**
     * The name of the user. Conflicts with `role`.
     */
    public readonly user!: pulumi.Output<string | undefined>;

    /**
     * Create a Grant resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GrantArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GrantArgs | GrantState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as GrantState | undefined;
            inputs["database"] = state ? state.database : undefined;
            inputs["grant"] = state ? state.grant : undefined;
            inputs["host"] = state ? state.host : undefined;
            inputs["privileges"] = state ? state.privileges : undefined;
            inputs["role"] = state ? state.role : undefined;
            inputs["roles"] = state ? state.roles : undefined;
            inputs["table"] = state ? state.table : undefined;
            inputs["tlsOption"] = state ? state.tlsOption : undefined;
            inputs["user"] = state ? state.user : undefined;
        } else {
            const args = argsOrState as GrantArgs | undefined;
            if (!args || args.database === undefined) {
                throw new Error("Missing required property 'database'");
            }
            inputs["database"] = args ? args.database : undefined;
            inputs["grant"] = args ? args.grant : undefined;
            inputs["host"] = args ? args.host : undefined;
            inputs["privileges"] = args ? args.privileges : undefined;
            inputs["role"] = args ? args.role : undefined;
            inputs["roles"] = args ? args.roles : undefined;
            inputs["table"] = args ? args.table : undefined;
            inputs["tlsOption"] = args ? args.tlsOption : undefined;
            inputs["user"] = args ? args.user : undefined;
        }
        super(Grant.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Grant resources.
 */
export interface GrantState {
    /**
     * The database to grant privileges on.
     */
    readonly database?: pulumi.Input<string>;
    /**
     * Whether to also give the user privileges to grant the same privileges to other users.
     */
    readonly grant?: pulumi.Input<boolean>;
    /**
     * The source host of the user. Defaults to "localhost". Conflicts with `role`.
     */
    readonly host?: pulumi.Input<string>;
    /**
     * A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
     */
    readonly privileges?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The role to grant `privileges` to. Conflicts with `user` and `host`.
     */
    readonly role?: pulumi.Input<string>;
    /**
     * A list of rols to grant to the user. Conflicts with `privileges`.
     */
    readonly roles?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Which table to grant `privileges` on. Defaults to `*`, which is all tables.
     */
    readonly table?: pulumi.Input<string>;
    /**
     * An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
     */
    readonly tlsOption?: pulumi.Input<string>;
    /**
     * The name of the user. Conflicts with `role`.
     */
    readonly user?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Grant resource.
 */
export interface GrantArgs {
    /**
     * The database to grant privileges on.
     */
    readonly database: pulumi.Input<string>;
    /**
     * Whether to also give the user privileges to grant the same privileges to other users.
     */
    readonly grant?: pulumi.Input<boolean>;
    /**
     * The source host of the user. Defaults to "localhost". Conflicts with `role`.
     */
    readonly host?: pulumi.Input<string>;
    /**
     * A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
     */
    readonly privileges?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The role to grant `privileges` to. Conflicts with `user` and `host`.
     */
    readonly role?: pulumi.Input<string>;
    /**
     * A list of rols to grant to the user. Conflicts with `privileges`.
     */
    readonly roles?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Which table to grant `privileges` on. Defaults to `*`, which is all tables.
     */
    readonly table?: pulumi.Input<string>;
    /**
     * An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
     */
    readonly tlsOption?: pulumi.Input<string>;
    /**
     * The name of the user. Conflicts with `role`.
     */
    readonly user?: pulumi.Input<string>;
}
