// Copyright (c) OpenFaaS Author(s) 2018. All rights reserved.
// Licensed under the MIT license. See LICENSE file in the project root for full license information.
package com.openfaas.model;

public abstract class AbstractHandler implements IHandler {
    public abstract IResponse Handle(IRequest request);
}
