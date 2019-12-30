// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;

namespace Pulumi.MySql
{
    public static class Config
    {
        private static readonly Pulumi.Config __config = new Pulumi.Config("mysql");

        public static string? AuthenticationPlugin { get; set; } = __config.Get("authenticationPlugin");

        public static string? Endpoint { get; set; } = __config.Get("endpoint") ?? Utilities.GetEnv("MYSQL_ENDPOINT");

        public static int? MaxConnLifetimeSec { get; set; } = __config.GetInt32("maxConnLifetimeSec");

        public static int? MaxOpenConns { get; set; } = __config.GetInt32("maxOpenConns");

        public static string? Password { get; set; } = __config.Get("password") ?? Utilities.GetEnv("MYSQL_PASSWORD");

        public static string? Proxy { get; set; } = __config.Get("proxy") ?? Utilities.GetEnv("ALL_PROXY", "all_proxy");

        public static string? Tls { get; set; } = __config.Get("tls") ?? Utilities.GetEnv("MYSQL_TLS_CONFIG") ?? "false";

        public static string? Username { get; set; } = __config.Get("username") ?? Utilities.GetEnv("MYSQL_USERNAME");

    }
    namespace ConfigTypes
    {
    }
}
