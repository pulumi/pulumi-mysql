// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

declare var exports: any;
const __config = new pulumi.Config("mysql");

export declare const authenticationPlugin: string | undefined;
Object.defineProperty(exports, "authenticationPlugin", {
    get() {
        return __config.get("authenticationPlugin");
    },
    enumerable: true,
});

export declare const endpoint: string | undefined;
Object.defineProperty(exports, "endpoint", {
    get() {
        return __config.get("endpoint");
    },
    enumerable: true,
});

export declare const maxConnLifetimeSec: number | undefined;
Object.defineProperty(exports, "maxConnLifetimeSec", {
    get() {
        return __config.getObject<number>("maxConnLifetimeSec");
    },
    enumerable: true,
});

export declare const maxOpenConns: number | undefined;
Object.defineProperty(exports, "maxOpenConns", {
    get() {
        return __config.getObject<number>("maxOpenConns");
    },
    enumerable: true,
});

export declare const password: string | undefined;
Object.defineProperty(exports, "password", {
    get() {
        return __config.get("password");
    },
    enumerable: true,
});

export declare const proxy: string | undefined;
Object.defineProperty(exports, "proxy", {
    get() {
        return __config.get("proxy") ?? utilities.getEnv("ALL_PROXY", "all_proxy");
    },
    enumerable: true,
});

export declare const tls: string;
Object.defineProperty(exports, "tls", {
    get() {
        return __config.get("tls") ?? (utilities.getEnv("MYSQL_TLS_CONFIG") || "false");
    },
    enumerable: true,
});

export declare const username: string | undefined;
Object.defineProperty(exports, "username", {
    get() {
        return __config.get("username");
    },
    enumerable: true,
});

