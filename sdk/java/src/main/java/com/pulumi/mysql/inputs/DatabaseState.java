// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.mysql.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class DatabaseState extends com.pulumi.resources.ResourceArgs {

    public static final DatabaseState Empty = new DatabaseState();

    /**
     * The default character set to use when
     * a table is created without specifying an explicit character set. Defaults
     * to &#34;utf8&#34;.
     * 
     */
    @Import(name="defaultCharacterSet")
    private @Nullable Output<String> defaultCharacterSet;

    /**
     * @return The default character set to use when
     * a table is created without specifying an explicit character set. Defaults
     * to &#34;utf8&#34;.
     * 
     */
    public Optional<Output<String>> defaultCharacterSet() {
        return Optional.ofNullable(this.defaultCharacterSet);
    }

    /**
     * The default collation to use when a table
     * is created without specifying an explicit collation. Defaults to
     * ``utf8_general_ci``. Each character set has its own set of collations, so
     * changing the character set requires also changing the collation.
     * 
     */
    @Import(name="defaultCollation")
    private @Nullable Output<String> defaultCollation;

    /**
     * @return The default collation to use when a table
     * is created without specifying an explicit collation. Defaults to
     * ``utf8_general_ci``. Each character set has its own set of collations, so
     * changing the character set requires also changing the collation.
     * 
     */
    public Optional<Output<String>> defaultCollation() {
        return Optional.ofNullable(this.defaultCollation);
    }

    /**
     * The name of the database. This must be unique within
     * a given MySQL server and may or may not be case-sensitive depending on
     * the operating system on which the MySQL server is running.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The name of the database. This must be unique within
     * a given MySQL server and may or may not be case-sensitive depending on
     * the operating system on which the MySQL server is running.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    private DatabaseState() {}

    private DatabaseState(DatabaseState $) {
        this.defaultCharacterSet = $.defaultCharacterSet;
        this.defaultCollation = $.defaultCollation;
        this.name = $.name;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DatabaseState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DatabaseState $;

        public Builder() {
            $ = new DatabaseState();
        }

        public Builder(DatabaseState defaults) {
            $ = new DatabaseState(Objects.requireNonNull(defaults));
        }

        /**
         * @param defaultCharacterSet The default character set to use when
         * a table is created without specifying an explicit character set. Defaults
         * to &#34;utf8&#34;.
         * 
         * @return builder
         * 
         */
        public Builder defaultCharacterSet(@Nullable Output<String> defaultCharacterSet) {
            $.defaultCharacterSet = defaultCharacterSet;
            return this;
        }

        /**
         * @param defaultCharacterSet The default character set to use when
         * a table is created without specifying an explicit character set. Defaults
         * to &#34;utf8&#34;.
         * 
         * @return builder
         * 
         */
        public Builder defaultCharacterSet(String defaultCharacterSet) {
            return defaultCharacterSet(Output.of(defaultCharacterSet));
        }

        /**
         * @param defaultCollation The default collation to use when a table
         * is created without specifying an explicit collation. Defaults to
         * ``utf8_general_ci``. Each character set has its own set of collations, so
         * changing the character set requires also changing the collation.
         * 
         * @return builder
         * 
         */
        public Builder defaultCollation(@Nullable Output<String> defaultCollation) {
            $.defaultCollation = defaultCollation;
            return this;
        }

        /**
         * @param defaultCollation The default collation to use when a table
         * is created without specifying an explicit collation. Defaults to
         * ``utf8_general_ci``. Each character set has its own set of collations, so
         * changing the character set requires also changing the collation.
         * 
         * @return builder
         * 
         */
        public Builder defaultCollation(String defaultCollation) {
            return defaultCollation(Output.of(defaultCollation));
        }

        /**
         * @param name The name of the database. This must be unique within
         * a given MySQL server and may or may not be case-sensitive depending on
         * the operating system on which the MySQL server is running.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The name of the database. This must be unique within
         * a given MySQL server and may or may not be case-sensitive depending on
         * the operating system on which the MySQL server is running.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        public DatabaseState build() {
            return $;
        }
    }

}
