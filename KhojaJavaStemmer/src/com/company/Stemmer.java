package com.company;

import khoja.ArabicStemmerKhoja;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Stemmer {
    List<String> stopwordsList;
    ArabicStemmerKhoja mystemmer;

    public Stemmer() {

        // load stopwords
        String stopwords = null;
        try {
            stopwords = new Scanner(Paths.get("stopwords.txt"), "UTF-8").useDelimiter("\\A").next();
        } catch (IOException e) {
            e.printStackTrace();
        }

        stopwordsList = Arrays.asList(stopwords.split("\n"));

        mystemmer = new ArabicStemmerKhoja();
    }

    public String stem(String tweet) {
        // check command-line argument
        if (tweet.isEmpty()) {
            System.out.println("ERROR: Empty Tweet");
            return "-1";
        }

        String[] tokenizedTweet = tweet.split("\\s");

        StringBuilder lineout = new StringBuilder();
        try {

            for (String token : tokenizedTweet) {

                if (!stopwordsList.contains(token)) {    // ignore stopwords
                    String result = mystemmer.stem(token);    // Khoja rooting algorithm
                    lineout.append(result).append(" ");
                }
            }
        } catch (Exception e) {
            System.out.println(Arrays.toString(e.getStackTrace()));
        }

        return lineout.toString().trim();
    }
}