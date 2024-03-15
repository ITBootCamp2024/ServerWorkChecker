package com.example.ITCluster2024.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
public class ITCamp {
    @GetMapping ("/getPage")
    public Object hello(){
        Map<String,String> object = new HashMap<>();
        object.put("name", "ItCluster");
        object.put("hello, World", "!");
        return object;
    }
}
