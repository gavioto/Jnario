/**
 * <copyright>
 * </copyright>
 *
 */
package de.bmw.carit.jnario.jnario;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>When</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * <ul>
 *   <li>{@link de.bmw.carit.jnario.jnario.When#getAnd <em>And</em>}</li>
 * </ul>
 * </p>
 *
 * @see de.bmw.carit.jnario.jnario.JnarioPackage#getWhen()
 * @model
 * @generated
 */
public interface When extends Step
{
	/**
	 * Returns the value of the '<em><b>And</b></em>' containment reference list.
	 * The list contents are of type {@link de.bmw.carit.jnario.jnario.And}.
	 * <!-- begin-user-doc -->
	 * <p>
	 * If the meaning of the '<em>And</em>' containment reference list isn't clear,
	 * there really should be more of a description here...
	 * </p>
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>And</em>' containment reference list.
	 * @see de.bmw.carit.jnario.jnario.JnarioPackage#getWhen_And()
	 * @model containment="true"
	 * @generated
	 */
	EList<And> getAnd();

} // When
