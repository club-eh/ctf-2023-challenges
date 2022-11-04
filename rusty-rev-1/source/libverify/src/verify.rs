use std::ffi::{c_char, CStr};

use super::constants::*;


#[inline]
/// Computes a couple of binary XORs and compares them against stored values.
fn check_xor_halves(input: &[u8]) -> bool {
	let halflen: usize = input.len() / 2;

	for i in 0..halflen {
		// block XOR (aaaaaa...bbbbbb...)
		if input[i] ^ input[i + halflen] != FLAG_BLOCK_XOR[i] {
			return false
		}
		// striped XOR (abababababab...)
		if input[i*2] ^ input[i*2+1] != FLAG_STRIPE_XOR[i] {
			return false
		}
	}

	return true
}


/// Returns true if the given data matches the flag, false otherwise.
pub(crate) fn verify_internal(data: &[u8]) -> bool {
	// check length
	if data.len() != FLAG_LEN {
		return false
	}

	// check flag prefix
	if !data.starts_with(b"clubeh") {
		return false
	}

	// requires FLAG_LEN % 4 == 2 to work properly
	return check_xor_halves(data)
}

/// C-compatible wrapper function to check if a given string matches the flag.
#[export_name = "verify_flag"]
pub unsafe extern "C" fn verify_flag_cstr(string: *const c_char) -> bool {
	verify_internal(CStr::from_ptr(string).to_bytes())
}
