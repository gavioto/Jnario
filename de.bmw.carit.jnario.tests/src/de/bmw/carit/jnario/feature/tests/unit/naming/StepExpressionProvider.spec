/*******************************************************************************
 * Copyright (c) 2012 BMW Car IT and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 *******************************************************************************/
package de.bmw.carit.jnario.feature.tests.unit.naming

import com.google.inject.Inject
import de.bmw.carit.jnario.common.test.util.ModelStore
import de.bmw.carit.jnario.common.test.util.SpecTestInstantiator
import de.bmw.carit.jnario.feature.feature.Step
import de.bmw.carit.jnario.feature.feature.StepReference
import de.bmw.carit.jnario.feature.naming.StepExpressionProvider
import de.bmw.carit.jnario.runner.InstantiateWith
import static de.bmw.carit.jnario.common.test.util.Query.*

/**
 * @author Sebastian Benz - Initial contribution and API
 */
@InstantiateWith(typeof(SpecTestInstantiator))
describe StepExpressionProvider{

	@Inject extension ModelStore modelStore
	
	it "should return the name for a step with definition"{
		parseScenario('''
			Feature: Example
				Scenario: MyScenario
					Given a step with an implementation
						"the implementation"
		''')
		assert step.stepExpression == subject.expressionOf(step)
	}
	
	it "should copy the referenced step's implementation and set the referencing step"{
		parseScenario('''
			Feature: Example
				Scenario: MyScenario 1
					Given a step 
						
				Scenario: MyScenario 2
					Given a step 
						"the implementation"
		''')
		val expr = subject.expressionOf(step)
		assert expr != null
		assert step.stepExpression == expr
		assert (step as StepReference).reference.stepExpression != expr
	}
	
	def step(){
		return query(modelStore).first(typeof(Step))
	}
}