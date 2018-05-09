package com.company;

import py4j.GatewayServer;

public class StackEntryPoint {

    private Stemmer stemmer;

    public StackEntryPoint() {
        stemmer = new Stemmer();
    }

    public Stemmer getStemmer() {
        return stemmer;
    }

    public static void main(String[] args) {
        GatewayServer gatewayServer = new GatewayServer(new StackEntryPoint());
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }

}
