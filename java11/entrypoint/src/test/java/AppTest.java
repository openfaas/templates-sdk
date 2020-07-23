// Copyright (c) OpenFaaS Author(s) 2018. All rights reserved.
// Licensed under the MIT license. See LICENSE file in the project root for full license information.

import org.junit.Test;
import static org.junit.Assert.*;

import com.openfaas.entrypoint.App;
import org.junit.Assert;
import org.junit.Test;
import org.junit.BeforeClass;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
public class AppTest {
   public static void main(String args[]){
       AppTest test = new AppTest();
       test.testAppHasAGreeting();
   }
     @Test
     public void testAppHasAGreeting(){
        try {
             App app = new App();
             URL url = new URL("http://localhost:8082"); // create url object for the given string
             HttpURLConnection connection = (HttpURLConnection) url.openConnection();
             connection.connect(); //connect

             String responseMessage = connection.getResponseMessage(); //here you get the response message
             int responseCode = connection.getResponseCode(); //this is http response code

             // Read in all of the post results into a String.
             BufferedReader br = new BufferedReader(new InputStreamReader((connection.getInputStream())));
             String actualGreeting = "";
             Boolean keepGoing = true;
             while (keepGoing) {
                 String currentLine = br.readLine();
                 if (currentLine == null) {
                     keepGoing = false;
                 } else {
                     actualGreeting += currentLine;
                 }
             }
             System.out.println("data: "+actualGreeting);
             connection.disconnect();

             Assert.assertEquals(200,responseCode);
             Assert.assertEquals("OK", responseMessage);
             Assert.assertEquals("Hello, World!", actualGreeting);

         }catch(Exception e){
            e.printStackTrace();
            fail("connection error");
        }
    }
}
