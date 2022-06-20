// Copyright (c) OpenFaaS Author(s) 2018. All rights reserved.
// Licensed under the MIT license. See LICENSE file in the project root for full license information.
package com.openfaas.model;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class ResponseTest {
    @Test
    public void testResponseHeaderSetGetValue() {
        Response r = new Response();

        r.setHeader("X-Key", "value");

        assertEquals("value", r.getHeader("X-Key"));
    }

    @Test
    public void testResponseHeaderGetValueKeyMissIsNull() {
        Response r = new Response();
        assertEquals(null, r.getHeader("No-Such-Key"));
    }

    @Test
    public void testResponseHeaderSetGetClearGetValue() {
        Response r = new Response();

        r.setHeader("X-Key", "value");
        r.setHeader("X-Key", null);

        assertEquals(null, r.getHeader("X-Key"));
    }

    @Test
    public void testResponseGetSetContentType() {
        Response r = new Response();

        r.setContentType("application/json");

        assertEquals("application/json", r.getContentType());
    }

    @Test
    public void testResponseStatusCodeDefaultValue() {
        Response r = new Response();
        assertEquals(200, r.getStatusCode());
    }

    @Test
    public void testResponseStatusCodeSetGetValue() {
        Response r = new Response();
        r.setStatusCode(404);
        assertEquals(404, r.getStatusCode());
    }
}
