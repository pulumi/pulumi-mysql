// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.MySql
{
    /// <summary>
    /// The ``mysql.Grant`` resource creates and manages privileges given to
    /// a user on a MySQL server.
    /// 
    /// ## Examples
    /// 
    /// ### Granting Privileges to a User
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using MySql = Pulumi.MySql;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var jdoe = new MySql.User("jdoe", new()
    ///     {
    ///         UserName = "jdoe",
    ///         Host = "example.com",
    ///         PlaintextPassword = "password",
    ///     });
    /// 
    ///     var jdoeGrant = new MySql.Grant("jdoe", new()
    ///     {
    ///         User = jdoe.UserName,
    ///         Host = jdoe.Host,
    ///         Database = "app",
    ///         Privileges = new[]
    ///         {
    ///             "SELECT",
    ///             "UPDATE",
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ### Granting Privileges to a Role
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using MySql = Pulumi.MySql;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var developer = new MySql.Role("developer", new()
    ///     {
    ///         Name = "developer",
    ///     });
    /// 
    ///     var developerGrant = new MySql.Grant("developer", new()
    ///     {
    ///         Role = developer.Name,
    ///         Database = "app",
    ///         Privileges = new[]
    ///         {
    ///             "SELECT",
    ///             "UPDATE",
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ### Adding a Role to a User
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using MySql = Pulumi.MySql;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var jdoe = new MySql.User("jdoe", new()
    ///     {
    ///         UserName = "jdoe",
    ///         Host = "example.com",
    ///         PlaintextPassword = "password",
    ///     });
    /// 
    ///     var developer = new MySql.Role("developer", new()
    ///     {
    ///         Name = "developer",
    ///     });
    /// 
    ///     var developerGrant = new MySql.Grant("developer", new()
    ///     {
    ///         User = jdoe.UserName,
    ///         Host = jdoe.Host,
    ///         Database = "app",
    ///         Roles = new[]
    ///         {
    ///             developer.Name,
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// </summary>
    [MySqlResourceType("mysql:index/grant:Grant")]
    public partial class Grant : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The database to grant privileges on.
        /// </summary>
        [Output("database")]
        public Output<string> Database { get; private set; } = null!;

        /// <summary>
        /// Whether to also give the user privileges to grant the same privileges to other users.
        /// </summary>
        [Output("grant")]
        public Output<bool?> GrantName { get; private set; } = null!;

        /// <summary>
        /// The source host of the user. Defaults to "localhost". Conflicts with `role`.
        /// </summary>
        [Output("host")]
        public Output<string?> Host { get; private set; } = null!;

        /// <summary>
        /// A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
        /// </summary>
        [Output("privileges")]
        public Output<ImmutableArray<string>> Privileges { get; private set; } = null!;

        /// <summary>
        /// The role to grant `privileges` to. Conflicts with `user` and `host`.
        /// </summary>
        [Output("role")]
        public Output<string?> Role { get; private set; } = null!;

        /// <summary>
        /// A list of rols to grant to the user. Conflicts with `privileges`.
        /// </summary>
        [Output("roles")]
        public Output<ImmutableArray<string>> Roles { get; private set; } = null!;

        /// <summary>
        /// Which table to grant `privileges` on. Defaults to `*`, which is all tables.
        /// </summary>
        [Output("table")]
        public Output<string?> Table { get; private set; } = null!;

        /// <summary>
        /// An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
        /// </summary>
        [Output("tlsOption")]
        public Output<string?> TlsOption { get; private set; } = null!;

        /// <summary>
        /// The name of the user. Conflicts with `role`.
        /// </summary>
        [Output("user")]
        public Output<string?> User { get; private set; } = null!;


        /// <summary>
        /// Create a Grant resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Grant(string name, GrantArgs args, CustomResourceOptions? options = null)
            : base("mysql:index/grant:Grant", name, args ?? new GrantArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Grant(string name, Input<string> id, GrantState? state = null, CustomResourceOptions? options = null)
            : base("mysql:index/grant:Grant", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Grant resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Grant Get(string name, Input<string> id, GrantState? state = null, CustomResourceOptions? options = null)
        {
            return new Grant(name, id, state, options);
        }
    }

    public sealed class GrantArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The database to grant privileges on.
        /// </summary>
        [Input("database", required: true)]
        public Input<string> Database { get; set; } = null!;

        /// <summary>
        /// Whether to also give the user privileges to grant the same privileges to other users.
        /// </summary>
        [Input("grant")]
        public Input<bool>? GrantName { get; set; }

        /// <summary>
        /// The source host of the user. Defaults to "localhost". Conflicts with `role`.
        /// </summary>
        [Input("host")]
        public Input<string>? Host { get; set; }

        [Input("privileges")]
        private InputList<string>? _privileges;

        /// <summary>
        /// A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
        /// </summary>
        public InputList<string> Privileges
        {
            get => _privileges ?? (_privileges = new InputList<string>());
            set => _privileges = value;
        }

        /// <summary>
        /// The role to grant `privileges` to. Conflicts with `user` and `host`.
        /// </summary>
        [Input("role")]
        public Input<string>? Role { get; set; }

        [Input("roles")]
        private InputList<string>? _roles;

        /// <summary>
        /// A list of rols to grant to the user. Conflicts with `privileges`.
        /// </summary>
        public InputList<string> Roles
        {
            get => _roles ?? (_roles = new InputList<string>());
            set => _roles = value;
        }

        /// <summary>
        /// Which table to grant `privileges` on. Defaults to `*`, which is all tables.
        /// </summary>
        [Input("table")]
        public Input<string>? Table { get; set; }

        /// <summary>
        /// An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
        /// </summary>
        [Input("tlsOption")]
        public Input<string>? TlsOption { get; set; }

        /// <summary>
        /// The name of the user. Conflicts with `role`.
        /// </summary>
        [Input("user")]
        public Input<string>? User { get; set; }

        public GrantArgs()
        {
        }
        public static new GrantArgs Empty => new GrantArgs();
    }

    public sealed class GrantState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The database to grant privileges on.
        /// </summary>
        [Input("database")]
        public Input<string>? Database { get; set; }

        /// <summary>
        /// Whether to also give the user privileges to grant the same privileges to other users.
        /// </summary>
        [Input("grant")]
        public Input<bool>? GrantName { get; set; }

        /// <summary>
        /// The source host of the user. Defaults to "localhost". Conflicts with `role`.
        /// </summary>
        [Input("host")]
        public Input<string>? Host { get; set; }

        [Input("privileges")]
        private InputList<string>? _privileges;

        /// <summary>
        /// A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
        /// </summary>
        public InputList<string> Privileges
        {
            get => _privileges ?? (_privileges = new InputList<string>());
            set => _privileges = value;
        }

        /// <summary>
        /// The role to grant `privileges` to. Conflicts with `user` and `host`.
        /// </summary>
        [Input("role")]
        public Input<string>? Role { get; set; }

        [Input("roles")]
        private InputList<string>? _roles;

        /// <summary>
        /// A list of rols to grant to the user. Conflicts with `privileges`.
        /// </summary>
        public InputList<string> Roles
        {
            get => _roles ?? (_roles = new InputList<string>());
            set => _roles = value;
        }

        /// <summary>
        /// Which table to grant `privileges` on. Defaults to `*`, which is all tables.
        /// </summary>
        [Input("table")]
        public Input<string>? Table { get; set; }

        /// <summary>
        /// An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of 'SSL' will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
        /// </summary>
        [Input("tlsOption")]
        public Input<string>? TlsOption { get; set; }

        /// <summary>
        /// The name of the user. Conflicts with `role`.
        /// </summary>
        [Input("user")]
        public Input<string>? User { get; set; }

        public GrantState()
        {
        }
        public static new GrantState Empty => new GrantState();
    }
}
