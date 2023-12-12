// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.mysql;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.mysql.ProviderArgs;
import com.pulumi.mysql.Utilities;
import java.lang.String;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * The provider type for the mysql package. By default, resources use package-wide configuration
 * settings, however an explicit `Provider` instance may be created and passed during resource
 * construction to achieve fine-grained programmatic control over provider settings. See the
 * [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
 * 
 */
@ResourceType(type="pulumi:providers:mysql")
public class Provider extends com.pulumi.resources.ProviderResource {
    @Export(name="authenticationPlugin", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> authenticationPlugin;

    public Output<Optional<String>> authenticationPlugin() {
        return Codegen.optional(this.authenticationPlugin);
    }
    @Export(name="endpoint", refs={String.class}, tree="[0]")
    private Output<String> endpoint;

    public Output<String> endpoint() {
        return this.endpoint;
    }
    @Export(name="password", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> password;

    public Output<Optional<String>> password() {
        return Codegen.optional(this.password);
    }
    @Export(name="proxy", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> proxy;

    public Output<Optional<String>> proxy() {
        return Codegen.optional(this.proxy);
    }
    @Export(name="tls", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> tls;

    public Output<Optional<String>> tls() {
        return Codegen.optional(this.tls);
    }
    @Export(name="username", refs={String.class}, tree="[0]")
    private Output<String> username;

    public Output<String> username() {
        return this.username;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Provider(String name) {
        this(name, ProviderArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Provider(String name, ProviderArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Provider(String name, ProviderArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("mysql", name, args == null ? ProviderArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

}
