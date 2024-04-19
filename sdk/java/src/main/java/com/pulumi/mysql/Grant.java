// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.mysql;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.mysql.GrantArgs;
import com.pulumi.mysql.Utilities;
import com.pulumi.mysql.inputs.GrantState;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * The ``mysql.Grant`` resource creates and manages privileges given to
 * a user on a MySQL server.
 * 
 * ## Examples
 * 
 * ### Granting Privileges to a User
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.mysql.User;
 * import com.pulumi.mysql.UserArgs;
 * import com.pulumi.mysql.Grant;
 * import com.pulumi.mysql.GrantArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         var jdoe = new User(&#34;jdoe&#34;, UserArgs.builder()        
 *             .user(&#34;jdoe&#34;)
 *             .host(&#34;example.com&#34;)
 *             .plaintextPassword(&#34;password&#34;)
 *             .build());
 * 
 *         var jdoeGrant = new Grant(&#34;jdoeGrant&#34;, GrantArgs.builder()        
 *             .user(jdoe.user())
 *             .host(jdoe.host())
 *             .database(&#34;app&#34;)
 *             .privileges(            
 *                 &#34;SELECT&#34;,
 *                 &#34;UPDATE&#34;)
 *             .build());
 * 
 *     }
 * }
 * ```
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 * ### Granting Privileges to a Role
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.mysql.Role;
 * import com.pulumi.mysql.RoleArgs;
 * import com.pulumi.mysql.Grant;
 * import com.pulumi.mysql.GrantArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         var developer = new Role(&#34;developer&#34;, RoleArgs.builder()        
 *             .name(&#34;developer&#34;)
 *             .build());
 * 
 *         var developerGrant = new Grant(&#34;developerGrant&#34;, GrantArgs.builder()        
 *             .role(developer.name())
 *             .database(&#34;app&#34;)
 *             .privileges(            
 *                 &#34;SELECT&#34;,
 *                 &#34;UPDATE&#34;)
 *             .build());
 * 
 *     }
 * }
 * ```
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 * ### Adding a Role to a User
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.mysql.User;
 * import com.pulumi.mysql.UserArgs;
 * import com.pulumi.mysql.Role;
 * import com.pulumi.mysql.RoleArgs;
 * import com.pulumi.mysql.Grant;
 * import com.pulumi.mysql.GrantArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         var jdoe = new User(&#34;jdoe&#34;, UserArgs.builder()        
 *             .user(&#34;jdoe&#34;)
 *             .host(&#34;example.com&#34;)
 *             .plaintextPassword(&#34;password&#34;)
 *             .build());
 * 
 *         var developer = new Role(&#34;developer&#34;, RoleArgs.builder()        
 *             .name(&#34;developer&#34;)
 *             .build());
 * 
 *         var developerGrant = new Grant(&#34;developerGrant&#34;, GrantArgs.builder()        
 *             .user(jdoe.user())
 *             .host(jdoe.host())
 *             .database(&#34;app&#34;)
 *             .roles(developer.name())
 *             .build());
 * 
 *     }
 * }
 * ```
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 */
@ResourceType(type="mysql:index/grant:Grant")
public class Grant extends com.pulumi.resources.CustomResource {
    /**
     * The database to grant privileges on.
     * 
     */
    @Export(name="database", refs={String.class}, tree="[0]")
    private Output<String> database;

    /**
     * @return The database to grant privileges on.
     * 
     */
    public Output<String> database() {
        return this.database;
    }
    /**
     * Whether to also give the user privileges to grant the same privileges to other users.
     * 
     */
    @Export(name="grant", refs={Boolean.class}, tree="[0]")
    private Output</* @Nullable */ Boolean> grant;

    /**
     * @return Whether to also give the user privileges to grant the same privileges to other users.
     * 
     */
    public Output<Optional<Boolean>> grant() {
        return Codegen.optional(this.grant);
    }
    /**
     * The source host of the user. Defaults to &#34;localhost&#34;. Conflicts with `role`.
     * 
     */
    @Export(name="host", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> host;

    /**
     * @return The source host of the user. Defaults to &#34;localhost&#34;. Conflicts with `role`.
     * 
     */
    public Output<Optional<String>> host() {
        return Codegen.optional(this.host);
    }
    /**
     * A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
     * 
     */
    @Export(name="privileges", refs={List.class,String.class}, tree="[0,1]")
    private Output</* @Nullable */ List<String>> privileges;

    /**
     * @return A list of privileges to grant to the user. Refer to a list of privileges (such as [here](https://dev.mysql.com/doc/refman/5.5/en/grant.html)) for applicable privileges. Conflicts with `roles`.
     * 
     */
    public Output<Optional<List<String>>> privileges() {
        return Codegen.optional(this.privileges);
    }
    /**
     * The role to grant `privileges` to. Conflicts with `user` and `host`.
     * 
     */
    @Export(name="role", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> role;

    /**
     * @return The role to grant `privileges` to. Conflicts with `user` and `host`.
     * 
     */
    public Output<Optional<String>> role() {
        return Codegen.optional(this.role);
    }
    /**
     * A list of rols to grant to the user. Conflicts with `privileges`.
     * 
     */
    @Export(name="roles", refs={List.class,String.class}, tree="[0,1]")
    private Output</* @Nullable */ List<String>> roles;

    /**
     * @return A list of rols to grant to the user. Conflicts with `privileges`.
     * 
     */
    public Output<Optional<List<String>>> roles() {
        return Codegen.optional(this.roles);
    }
    /**
     * Which table to grant `privileges` on. Defaults to `*`, which is all tables.
     * 
     */
    @Export(name="table", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> table;

    /**
     * @return Which table to grant `privileges` on. Defaults to `*`, which is all tables.
     * 
     */
    public Output<Optional<String>> table() {
        return Codegen.optional(this.table);
    }
    /**
     * An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of &#39;SSL&#39; will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
     * 
     */
    @Export(name="tlsOption", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> tlsOption;

    /**
     * @return An TLS-Option for the `GRANT` statement. The value is suffixed to `REQUIRE`. A value of &#39;SSL&#39; will generate a `GRANT ... REQUIRE SSL` statement. See the [MYSQL `GRANT` documentation](https://dev.mysql.com/doc/refman/5.7/en/grant.html) for more. Ignored if MySQL version is under 5.7.0.
     * 
     */
    public Output<Optional<String>> tlsOption() {
        return Codegen.optional(this.tlsOption);
    }
    /**
     * The name of the user. Conflicts with `role`.
     * 
     */
    @Export(name="user", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> user;

    /**
     * @return The name of the user. Conflicts with `role`.
     * 
     */
    public Output<Optional<String>> user() {
        return Codegen.optional(this.user);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Grant(String name) {
        this(name, GrantArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Grant(String name, GrantArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Grant(String name, GrantArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("mysql:index/grant:Grant", name, args == null ? GrantArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private Grant(String name, Output<String> id, @Nullable GrantState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("mysql:index/grant:Grant", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static Grant get(String name, Output<String> id, @Nullable GrantState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Grant(name, id, state, options);
    }
}
