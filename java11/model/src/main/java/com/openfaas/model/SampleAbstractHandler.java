// Copyright (c) OpenFaaS Author(s) 2018. All rights reserved.
// Licensed under the MIT license. See LICENSE file in the project root for full license information.

package com.openfaas.model;

public class SampleAbstractHandler extends AbstractHandler {
    @Override
    public IResponse Handle(IRequest request) {
        Response resp = new Response();
        resp.setStatusCode(200);
        resp.setBody("Hello, World! From Kamesh");
        return resp;
    }
}
