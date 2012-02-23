/*******************************************************************************
 * Copyright (c) 2012 BMW Car IT and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 *******************************************************************************/
package de.bmw.carit.jnario.tests

import static de.bmw.carit.jnario.common.test.util.ResultMatchers.*
import static extension de.bmw.carit.jnario.common.test.util.FeatureExecutor.*

/**
 * @author Birgit Engelmann - Initial contribution and API
 */
Feature: Backgrounds

	Scenario: It is possible to add a background to a feature
		Given I have a feature with a background
			var jnarioFile = "
				package bootstrap
				Feature: Some feature
					Background:
						Given a user name
					Scenario: Scenario 1
					Scenario: Scenario 2
			"
		When I run the feature
		Then it should be successful
			jnarioFile.execute.should.be(successful)
			

	Scenario: Given methods from backgrounds are generated in every scenario class
	
		Given I have a feature with a background
			var jnarioFile = "
				package bootstrap
				Feature: Some feature
					Background:
						Given a user name
							throw new RuntimeException()
					Scenario: Scenario 1
					Scenario: Scenario 2
			"
		When I generate the classes
		Then every class should have a method that throws a RuntimeExeception
			jnarioFile.execute.failureCount.should.be(2)
			
			
			