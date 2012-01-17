/*******************************************************************************
 * Copyright (c) 2012 BMW Car IT and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 *******************************************************************************/
package de.bmw.carit.jnario.runner;

/**
 * @author Sebastian Benz
 */
public class DefaultTestInstantiator implements TestInstantiator {

	@Override
	public Object createTest(Class<?> klass) throws Exception {
		return klass.newInstance();
	}

	@Override
	public void beforeTestRun() {
	}

	@Override
	public void afterTestRun() {
	}

}
