package org.jnario.feature.tests.unit.contentassist

import org.jnario.feature.ui.contentassist.FeatureProposalProvider
import org.jnario.feature.FeatureUiInjectorProvider
import org.eclipse.xtext.junit4.InjectWith
import org.junit.runner.RunWith
import org.eclipse.xtext.junit4.XtextRunner
import org.jnario.runner.Extends
import org.eclipse.xtext.junit4.ui.AbstractContentAssistProcessorTest
import org.jnario.feature.FeatureStandaloneSetup
import org.jnario.runner.CreateWith
import org.jnario.jnario.test.util.FeatureUiTestCreator
import org.jnario.jnario.test.util.AbstractContentAssistProcessorTest2
import org.jnario.jnario.test.util.AbstractContentAssistProcessorTest2$ContentAssistProcessorTestBuilder2

@Extends(typeof(AbstractContentAssistProcessorTest2))
describe "FeatureProposalProvider"{
	
	ContentAssistProcessorTestBuilder2 builder
	
	context "same file"{
		fact "proposes implemented steps"{
			val builder = newBuilder.append('''
				Feature: My Feature
					Scenario: My Scenario
					Given an implemented step
						1 + 1 => 2
					
			''')
			builder.assertProposal("features.And an implemented step")
			builder.assertProposal("features.But an implemented step")
		}
		
		fact "proposes unimplemented steps"{
			val builder = newBuilder.append('''
				Feature: My Feature
					Scenario: My Scenario
					Given a pending step
					
			''')
			builder.assertProposal("features.And a pending step")
			builder.assertProposal("features.But a pending step")
		}
		
		fact "does not provide given for then"{
			val builder = newBuilder.append('''
				Feature: My Feature
					Scenario: My Scenario
					Given a step
					Then another step
					
			''')
			builder.assertProposalsContainNot("And a step")
			builder.assertProposal("features.And another step")
			builder.assertProposal("features.But another step")
		}
	}
	
	
	
	override protected doGetSetup() {
		new FeatureUiStandaloneSetup
	}
	
}