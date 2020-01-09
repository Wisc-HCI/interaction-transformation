import prism.Prism;
import prism.PrismDevNullLog;
import prism.PrismException;
import prism.PrismFileLog;
import prism.PrismLangException;
import java.io.FileNotFoundException;
import java.io.File;
import prism.PrismLog;
import parser.ast.ModulesFile;
import parser.ast.PropertiesFile;
import prism.Result;

import java.util.Scanner;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.lang.Thread;

public class RunPrism {

	static Thread sent;
    static Thread receive;
    static Socket socket;

	public static void main(String[] args) {

		try {
			System.out.println(Integer.parseInt(args[0]));
			socket = new Socket("localhost",Integer.parseInt(args[0]));
		} catch (UnknownHostException e1) {
			// TODO Auto-generated catch block
			 e1.printStackTrace();
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}

		try {
			// Create a log for PRISM output (hidden or stdout)
			PrismLog mainLog = new PrismDevNullLog();
			//PrismLog mainLog = new PrismFileLog("stdout");

			// Initialise PRISM engine
			Prism prism = new Prism(mainLog);
			prism.initialise();

			sent = new Thread(new Runnable() {
				@Override
				public void run() {
					try {
						BufferedReader stdIn =new BufferedReader(new InputStreamReader(socket.getInputStream()));
						PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

						out.print("Prism successfully initialized.\n");
						out.flush();

						while(true) {
							System.out.println("Waiting for model...");

							String modelFile = stdIn.readLine();
							out.print("Received model file: " + modelFile);
							System.out.println("Received model file " + modelFile);
							out.flush();

							File prismFile = new File(modelFile);

							ModulesFile modulesFile = null;
							PropertiesFile propertiesFile = null;
							Result rawResult = null;

							try {
								modulesFile = prism.parseModelFile(prismFile);
								prism.loadPRISMModel(modulesFile);

								// loop through and check properties
								String property = "";
								while (true) {
									System.out.println("reading a property (" + Integer.parseInt(args[0]) + ")");
									property = stdIn.readLine();
									System.out.println("read property " + property + "(" + Integer.parseInt(args[0]) + ")");
									if (property.equals("EOP"))
										break;
									else if (property.contains("ENGINE")) {
										if (property.contains("SPARSE")) {
											out.print("Setting engine to sparse");
											out.flush();
											Thread.sleep(10);
											prism.setEngine(Prism.SPARSE);
											out.print("Done");
											out.flush();
										}
										else if (property.contains("HYBRID")) {
											out.print("Setting engine to hybrid");
											out.flush();
											Thread.sleep(10);
											prism.setEngine(Prism.HYBRID);
											out.print("Done");
											out.flush();
										}
									}
									else if (property.contains("FAIRNESS")) {
										if (property.contains("TRUE")) {
											out.print("Setting fairness to true");
											out.flush();
											Thread.sleep(10);
											prism.setFairness(true);
											out.print("Done");
											out.flush();
										}
										else {
											out.print("Setting fairness to false");
											out.flush();
											Thread.sleep(10);
											prism.setFairness(false);
											out.print("Done");
											out.flush();
										}
									}
									else {
										//System.out.println("Received property" + property);
										out.print("Received property: " + property);
										out.flush();
										//Thread.sleep(10);

										// wait for input to proceed
										//String proceed = stdIn.readLine();

										propertiesFile = prism.parsePropertiesString(modulesFile, property);
										String toReturn = "";
										if (property.contains("filter")) {
											try {
												rawResult = prism.modelCheck(propertiesFile, propertiesFile.getPropertyObject(0));
												toReturn = rawResult.toString();
											} catch (PrismException e) {
												System.out.println("Caught exception");
												toReturn = "true";
											}
										}
										else if (property.contains("R{\"pos\"}=?") || property.contains("R{\"neg\"}=?") || property.contains("R{\"rob\"}=?") || property.contains("R{\"hum\"}=?")) {
											try {
												rawResult = prism.modelCheck(propertiesFile, propertiesFile.getPropertyObject(0));
												toReturn = rawResult.toString();
											} catch (PrismException e) {
												e.printStackTrace();
												System.out.println("Caught it appropriately");
												toReturn = "-10000000";
											}
										}
										else {
											rawResult = prism.modelCheck(propertiesFile, propertiesFile.getPropertyObject(0));
											//toReturn = "RESULT:"+rawResult.toString();
											toReturn = rawResult.toString();
										}
										mainLog.flush();
										//System.out.println("Checked property");
										Thread.sleep(15);
										out.print(toReturn);
										out.flush();
									}
								}

								//propertiesFile = prism.parsePropertiesString(modulesFile, property);
								//rawResult = prism.modelCheck(propertiesFile, propertiesFile.getPropertyObject(0));
								//mainLog.flush();
								//System.out.println(in);
								//out.print(rawResult.toString());
								//out.flush();
								//System.out.println("Message sent");
							} catch (FileNotFoundException | PrismLangException e1) {
								// TODO Auto-generated catch block
								e1.printStackTrace();

							} catch (PrismException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
								StringWriter errors = new StringWriter();
								e.printStackTrace(new PrintWriter(errors));
								String errorString = errors.toString();

								if (errorString.contains("Error: Iterative method did not converge within 10000 iterations"))
									System.out.println("Caught it");

							} catch (InterruptedException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							}
						}

					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}


				}
			});

			sent.start();
			try {
				sent.join();
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

			/*
			Scanner scanner = new Scanner(System.in);
			while (true) {
				while (!scanner.hasNext()) {System.out.println("waiting...");}
				//System.out.println("found output");
				String input = scanner.next();

				System.out.println(input);

				if (input.equals("exit"))
					break;

			}
			*/
		} catch (PrismException e) {
			System.out.println("Error: " + e.getMessage());
			System.exit(1);
		}
	}
}
