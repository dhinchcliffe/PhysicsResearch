import Mathlib

/-
DRAFT — NOT KERNEL-CHECKED IN THIS ENVIRONMENT.
These algebra statements are small proof targets, not physics claims.
No use of `sorry` or `admit`; successful compilation has not been established.
-/
namespace GravityWitness

variable {K : Type*} [Field K]

def Factors (a b c d : K) : Prop :=
  ∃ u0 u1 v0 v1 : K,
    a = u0 * v0 ∧ b = u0 * v1 ∧ c = u1 * v0 ∧ d = u1 * v1

theorem factors_implies_det_zero {a b c d : K}
    (h : Factors a b c d) : a * d - b * c = 0 := by
  rcases h with ⟨u0, u1, v0, v1, rfl, rfl, rfl, rfl⟩
  ring

/-- The nonzero upper-left pivot case; the other pivots remain a later target. -/
theorem det_zero_factors_nonzero_pivot {a b c d : K}
    (ha : a ≠ 0) (h : a * d - b * c = 0) : Factors a b c d := by
  have had : a * d = b * c := sub_eq_zero.mp h
  refine ⟨a, c, 1, b / a, ?_, ?_, ?_, ?_⟩
  · simp
  · field_simp [ha]
  · simp
  · field_simp [ha]
    calc
      d * a = a * d := mul_comm d a
      _ = b * c := had
      _ = c * b := mul_comm b c

/-- Local diagonal factors multiply the determinant by a common scalar. -/
theorem local_factors_det (a b c d u0 u1 v0 v1 : K) :
    (u0 * v0 * a) * (u1 * v1 * d) -
      (u0 * v1 * b) * (u1 * v0 * c) =
    (u0 * u1 * v0 * v1) * (a * d - b * c) := by
  ring

/-- Additive local phases cancel in the joint phase combination. -/
theorem phase_cancellation (p00 p01 p10 p11 a0 a1 b0 b1 : ℝ) :
    (p00 + a0 + b0) + (p11 + a1 + b1) -
      (p01 + a0 + b1) - (p10 + a1 + b0) =
    p00 + p11 - p01 - p10 := by
  ring

end GravityWitness
