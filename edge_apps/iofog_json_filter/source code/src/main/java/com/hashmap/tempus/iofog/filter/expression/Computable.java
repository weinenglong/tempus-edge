package com.hashmap.tempus.iofog.filter.expression;


import com.google.gson.JsonObject;

public interface Computable {
    public Boolean compute(JsonObject jsonObject);
}
