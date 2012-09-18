package org.jnario.jnario.tests.unit.report

import org.jnario.report.IsMatchingSpec
import org.jnario.report.Spec2ResultMapping

import static org.mockito.Mockito.*
import org.jnario.report.SpecExecution
import org.jnario.Specification
import static org.jnario.report.SpecExecution.*

describe Spec2ResultMapping {

	val isSpecPredicate = mock(typeof(IsMatchingSpec))
	
	val matchingResult = mock(typeof(SpecExecution))
	val notMatchingResult = mock(typeof(SpecExecution))
	val aSpec = mock(typeof(Specification))
	
	before subject = new Spec2ResultMapping(isSpecPredicate)
	
	fact "returns empty execution if no matching spec exists"{
		subject.getResult(aSpec) => NO_EXECUTION
	}
	
	fact "returns execution result matching to spec"{
		when(isSpecPredicate.matches(aSpec, matchingResult)).thenReturn(true)
		when(isSpecPredicate.matches(aSpec, notMatchingResult)).thenReturn(false)

		subject.accept(notMatchingResult)
		subject.accept(matchingResult)
		
		subject.getResult(aSpec) => matchingResult
	}

}