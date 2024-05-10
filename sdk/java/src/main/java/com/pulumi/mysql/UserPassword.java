// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.mysql;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.mysql.UserPasswordArgs;
import com.pulumi.mysql.Utilities;
import com.pulumi.mysql.inputs.UserPasswordState;
import java.lang.String;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * The `mysql.UserPassword` resource sets and manages a password for a given
 * user on a MySQL server.
 * 
 * &gt; **NOTE on MySQL Passwords:** This resource conflicts with the `password`
 *    argument for `mysql.User`. This resource uses PGP encryption to avoid
 *    storing unencrypted passwords in the provider state.
 * 
 * &gt; **NOTE on How Passwords are Created:** This resource **automatically**
 *    generates a **random** password. The password will be a random UUID.
 * 
 * ## Example Usage
 * 
 *  &lt;!--Start PulumiCodeChooser --&gt;
 * <pre>
 * {@code
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.mysql.User;
 * import com.pulumi.mysql.UserArgs;
 * import com.pulumi.mysql.UserPassword;
 * import com.pulumi.mysql.UserPasswordArgs;
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
 *         var jdoe = new User("jdoe", UserArgs.builder()        
 *             .user("jdoe")
 *             .build());
 * 
 *         var jdoeUserPassword = new UserPassword("jdoeUserPassword", UserPasswordArgs.builder()        
 *             .user(jdoe.user())
 *             .pgpKey("keybase:joestump")
 *             .build());
 * 
 *     }
 * }
 * }
 * </pre>
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 */
@ResourceType(type="mysql:index/userPassword:UserPassword")
public class UserPassword extends com.pulumi.resources.CustomResource {
    /**
     * The encrypted password, base64 encoded.
     * 
     */
    @Export(name="encryptedPassword", refs={String.class}, tree="[0]")
    private Output<String> encryptedPassword;

    /**
     * @return The encrypted password, base64 encoded.
     * 
     */
    public Output<String> encryptedPassword() {
        return this.encryptedPassword;
    }
    /**
     * The source host of the user. Defaults to `localhost`.
     * 
     */
    @Export(name="host", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> host;

    /**
     * @return The source host of the user. Defaults to `localhost`.
     * 
     */
    public Output<Optional<String>> host() {
        return Codegen.optional(this.host);
    }
    /**
     * The fingerprint of the PGP key used to encrypt the password
     * 
     */
    @Export(name="keyFingerprint", refs={String.class}, tree="[0]")
    private Output<String> keyFingerprint;

    /**
     * @return The fingerprint of the PGP key used to encrypt the password
     * 
     */
    public Output<String> keyFingerprint() {
        return this.keyFingerprint;
    }
    /**
     * Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
     * 
     */
    @Export(name="pgpKey", refs={String.class}, tree="[0]")
    private Output<String> pgpKey;

    /**
     * @return Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
     * 
     */
    public Output<String> pgpKey() {
        return this.pgpKey;
    }
    /**
     * The IAM user to associate with this access key.
     * 
     */
    @Export(name="user", refs={String.class}, tree="[0]")
    private Output<String> user;

    /**
     * @return The IAM user to associate with this access key.
     * 
     */
    public Output<String> user() {
        return this.user;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public UserPassword(String name) {
        this(name, UserPasswordArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public UserPassword(String name, UserPasswordArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public UserPassword(String name, UserPasswordArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("mysql:index/userPassword:UserPassword", name, args == null ? UserPasswordArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private UserPassword(String name, Output<String> id, @Nullable UserPasswordState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("mysql:index/userPassword:UserPassword", name, state, makeResourceOptions(options, id));
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
    public static UserPassword get(String name, Output<String> id, @Nullable UserPasswordState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new UserPassword(name, id, state, options);
    }
}
