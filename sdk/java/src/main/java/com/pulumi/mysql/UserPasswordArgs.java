// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.mysql;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class UserPasswordArgs extends com.pulumi.resources.ResourceArgs {

    public static final UserPasswordArgs Empty = new UserPasswordArgs();

    /**
     * The source host of the user. Defaults to `localhost`.
     * 
     */
    @Import(name="host")
    private @Nullable Output<String> host;

    /**
     * @return The source host of the user. Defaults to `localhost`.
     * 
     */
    public Optional<Output<String>> host() {
        return Optional.ofNullable(this.host);
    }

    /**
     * Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
     * 
     */
    @Import(name="pgpKey", required=true)
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
    @Import(name="user", required=true)
    private Output<String> user;

    /**
     * @return The IAM user to associate with this access key.
     * 
     */
    public Output<String> user() {
        return this.user;
    }

    private UserPasswordArgs() {}

    private UserPasswordArgs(UserPasswordArgs $) {
        this.host = $.host;
        this.pgpKey = $.pgpKey;
        this.user = $.user;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(UserPasswordArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private UserPasswordArgs $;

        public Builder() {
            $ = new UserPasswordArgs();
        }

        public Builder(UserPasswordArgs defaults) {
            $ = new UserPasswordArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param host The source host of the user. Defaults to `localhost`.
         * 
         * @return builder
         * 
         */
        public Builder host(@Nullable Output<String> host) {
            $.host = host;
            return this;
        }

        /**
         * @param host The source host of the user. Defaults to `localhost`.
         * 
         * @return builder
         * 
         */
        public Builder host(String host) {
            return host(Output.of(host));
        }

        /**
         * @param pgpKey Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
         * 
         * @return builder
         * 
         */
        public Builder pgpKey(Output<String> pgpKey) {
            $.pgpKey = pgpKey;
            return this;
        }

        /**
         * @param pgpKey Either a base-64 encoded PGP public key, or a keybase username in the form `keybase:some_person_that_exists`.
         * 
         * @return builder
         * 
         */
        public Builder pgpKey(String pgpKey) {
            return pgpKey(Output.of(pgpKey));
        }

        /**
         * @param user The IAM user to associate with this access key.
         * 
         * @return builder
         * 
         */
        public Builder user(Output<String> user) {
            $.user = user;
            return this;
        }

        /**
         * @param user The IAM user to associate with this access key.
         * 
         * @return builder
         * 
         */
        public Builder user(String user) {
            return user(Output.of(user));
        }

        public UserPasswordArgs build() {
            if ($.pgpKey == null) {
                throw new MissingRequiredPropertyException("UserPasswordArgs", "pgpKey");
            }
            if ($.user == null) {
                throw new MissingRequiredPropertyException("UserPasswordArgs", "user");
            }
            return $;
        }
    }

}
