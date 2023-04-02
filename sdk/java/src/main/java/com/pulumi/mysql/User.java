// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.mysql;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.mysql.UserArgs;
import com.pulumi.mysql.Utilities;
import com.pulumi.mysql.inputs.UserState;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * The ``mysql.User`` resource creates and manages a user on a MySQL
 * server.
 * 
 * ## Examples
 * 
 * ### Basic Usage
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.mysql.User;
 * import com.pulumi.mysql.UserArgs;
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
 *             .host(&#34;example.com&#34;)
 *             .plaintextPassword(&#34;password&#34;)
 *             .user(&#34;jdoe&#34;)
 *             .build());
 * 
 *     }
 * }
 * ```
 * 
 * ### Example Usage with an Authentication Plugin
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.mysql.User;
 * import com.pulumi.mysql.UserArgs;
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
 *         var nologin = new User(&#34;nologin&#34;, UserArgs.builder()        
 *             .authPlugin(&#34;mysql_no_login&#34;)
 *             .host(&#34;example.com&#34;)
 *             .user(&#34;nologin&#34;)
 *             .build());
 * 
 *     }
 * }
 * ```
 * 
 */
@ResourceType(type="mysql:index/user:User")
public class User extends com.pulumi.resources.CustomResource {
    /**
     * Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintext_password`.
     * 
     */
    @Export(name="authPlugin", type=String.class, parameters={})
    private Output</* @Nullable */ String> authPlugin;

    /**
     * @return Use an [authentication plugin][ref-auth-plugins] to authenticate the user instead of using password authentication.  Description of the fields allowed in the block below. Conflicts with `password` and `plaintext_password`.
     * 
     */
    public Output<Optional<String>> authPlugin() {
        return Codegen.optional(this.authPlugin);
    }
    /**
     * The source host of the user. Defaults to &#34;localhost&#34;.
     * 
     */
    @Export(name="host", type=String.class, parameters={})
    private Output</* @Nullable */ String> host;

    /**
     * @return The source host of the user. Defaults to &#34;localhost&#34;.
     * 
     */
    public Output<Optional<String>> host() {
        return Codegen.optional(this.host);
    }
    /**
     * Deprecated alias of `plaintext_password`, whose value is *stored as plaintext in state*. Prefer to use `plaintext_password` instead, which stores the password as an unsalted hash. Conflicts with `auth_plugin`.
     * 
     * @deprecated
     * Please use plaintext_password instead
     * 
     */
    @Deprecated /* Please use plaintext_password instead */
    @Export(name="password", type=String.class, parameters={})
    private Output</* @Nullable */ String> password;

    /**
     * @return Deprecated alias of `plaintext_password`, whose value is *stored as plaintext in state*. Prefer to use `plaintext_password` instead, which stores the password as an unsalted hash. Conflicts with `auth_plugin`.
     * 
     */
    public Output<Optional<String>> password() {
        return Codegen.optional(this.password);
    }
    /**
     * The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `auth_plugin`.
     * 
     */
    @Export(name="plaintextPassword", type=String.class, parameters={})
    private Output</* @Nullable */ String> plaintextPassword;

    /**
     * @return The password for the user. This must be provided in plain text, so the data source for it must be secured. An _unsalted_ hash of the provided password is stored in state. Conflicts with `auth_plugin`.
     * 
     */
    public Output<Optional<String>> plaintextPassword() {
        return Codegen.optional(this.plaintextPassword);
    }
    /**
     * An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of &#39;SSL&#39; will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
     * 
     */
    @Export(name="tlsOption", type=String.class, parameters={})
    private Output</* @Nullable */ String> tlsOption;

    /**
     * @return An TLS-Option for the `CREATE USER` or `ALTER USER` statement. The value is suffixed to `REQUIRE`. A value of &#39;SSL&#39; will generate a `CREATE USER ... REQUIRE SSL` statement. See the [MYSQL `CREATE USER` documentation](https://dev.mysql.com/doc/refman/5.7/en/create-user.html) for more. Ignored if MySQL version is under 5.7.0.
     * 
     */
    public Output<Optional<String>> tlsOption() {
        return Codegen.optional(this.tlsOption);
    }
    /**
     * The name of the user.
     * 
     */
    @Export(name="user", type=String.class, parameters={})
    private Output<String> user;

    /**
     * @return The name of the user.
     * 
     */
    public Output<String> user() {
        return this.user;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public User(String name) {
        this(name, UserArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public User(String name, UserArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public User(String name, UserArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("mysql:index/user:User", name, args == null ? UserArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private User(String name, Output<String> id, @Nullable UserState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("mysql:index/user:User", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .additionalSecretOutputs(List.of(
                "password",
                "plaintextPassword"
            ))
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
    public static User get(String name, Output<String> id, @Nullable UserState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new User(name, id, state, options);
    }
}
