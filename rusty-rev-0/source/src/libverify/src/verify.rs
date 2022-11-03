use std::ffi::{c_char, CStr};

use super::constants::*;


/// Returns true if the given data matches the flag, false otherwise.
fn verify_internal(data: &[u8]) -> bool {
	// verify flag length
	if data.len() != FLAG_LEN {
		return false
	}

	// decode flag
	let decoded_flag: [u8; FLAG_LEN] = ENCODED_FLAG.map(|c| c ^ XOR_KEY);

	// compare flag
	return data == decoded_flag
}

/// C-compatible wrapper function to check if a given string matches the flag.
#[export_name = "verify_flag"]
pub unsafe extern "C" fn verify_flag_cstr(string: *const c_char) -> bool {
	verify_internal(CStr::from_ptr(string).to_bytes())
}
