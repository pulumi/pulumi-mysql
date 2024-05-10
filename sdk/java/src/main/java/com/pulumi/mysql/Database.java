// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.mysql;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.mysql.DatabaseArgs;
import com.pulumi.mysql.Utilities;
import com.pulumi.mysql.inputs.DatabaseState;
import java.lang.String;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * The ``mysql.Database`` resource creates and manages a database on a MySQL
 * server.
 * 
 * ## Example Usage
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * <pre>
 * {@code
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.mysql.Database;
 * import com.pulumi.mysql.DatabaseArgs;
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
 *         var app = new Database("app", DatabaseArgs.builder()        
 *             .name("my_awesome_app")
 *             .build());
 * 
 *     }
 * }
 * }
 * </pre>
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 * ## Import
 * 
 * Databases can be imported using their name, e.g.
 * 
 * ```sh
 * $ pulumi import mysql:index/database:Database example my-example-database
 * ```
 * 
 */
@ResourceType(type="mysql:index/database:Database")
public class Database extends com.pulumi.resources.CustomResource {
    /**
     * The default character set to use when
     * a table is created without specifying an explicit character set. Defaults
     * to &#34;utf8&#34;.
     * 
     */
    @Export(name="defaultCharacterSet", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> defaultCharacterSet;

    /**
     * @return The default character set to use when
     * a table is created without specifying an explicit character set. Defaults
     * to &#34;utf8&#34;.
     * 
     */
    public Output<Optional<String>> defaultCharacterSet() {
        return Codegen.optional(this.defaultCharacterSet);
    }
    /**
     * The default collation to use when a table
     * is created without specifying an explicit collation. Defaults to
     * ``utf8_general_ci``. Each character set has its own set of collations, so
     * changing the character set requires also changing the collation.
     * 
     * Note that the defaults for character set and collation above do not respect
     * any defaults set on the MySQL server, so that the configuration can be set
     * appropriately even though this provider cannot see the server-level defaults. If
     * you wish to use the server&#39;s defaults you must consult the server&#39;s
     * configuration and then set the ``default_character_set`` and
     * ``default_collation`` to match.
     * 
     */
    @Export(name="defaultCollation", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> defaultCollation;

    /**
     * @return The default collation to use when a table
     * is created without specifying an explicit collation. Defaults to
     * ``utf8_general_ci``. Each character set has its own set of collations, so
     * changing the character set requires also changing the collation.
     * 
     * Note that the defaults for character set and collation above do not respect
     * any defaults set on the MySQL server, so that the configuration can be set
     * appropriately even though this provider cannot see the server-level defaults. If
     * you wish to use the server&#39;s defaults you must consult the server&#39;s
     * configuration and then set the ``default_character_set`` and
     * ``default_collation`` to match.
     * 
     */
    public Output<Optional<String>> defaultCollation() {
        return Codegen.optional(this.defaultCollation);
    }
    /**
     * The name of the database. This must be unique within
     * a given MySQL server and may or may not be case-sensitive depending on
     * the operating system on which the MySQL server is running.
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return The name of the database. This must be unique within
     * a given MySQL server and may or may not be case-sensitive depending on
     * the operating system on which the MySQL server is running.
     * 
     */
    public Output<String> name() {
        return this.name;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Database(String name) {
        this(name, DatabaseArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Database(String name, @Nullable DatabaseArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Database(String name, @Nullable DatabaseArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("mysql:index/database:Database", name, args == null ? DatabaseArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private Database(String name, Output<String> id, @Nullable DatabaseState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("mysql:index/database:Database", name, state, makeResourceOptions(options, id));
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
    public static Database get(String name, Output<String> id, @Nullable DatabaseState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Database(name, id, state, options);
    }
}
