package com.company;

import py4j.GatewayServer;

public class StemmerEntryPoint {

    private Stemmer stemmer;

    public StemmerEntryPoint() {
        stemmer = new Stemmer();
    }

    public Stemmer getStemmer() {
        return stemmer;
    }

    public static void main(String[] args) {
        GatewayServer gatewayServer = new GatewayServer(new StemmerEntryPoint());
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }

}
