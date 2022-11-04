use std::ffi::{c_char, CStr};

use super::constants::*;


const FNV_1A_BASIS: u64 = 0xcbf29ce484222325;
const FNV_1A_PRIME: u64 = 0x00000100000001b3;


#[inline]
/// Computes a couple of binary XORs and compares them against stored values.
fn check_xor_halves(input: &[u8]) -> Result<(), ()> {
	let halflen: usize = input.len() / 2;

	for i in 0..halflen {
		// block XOR (aaaaaa...bbbbbb...)
		if input[i] ^ input[i + halflen] != FLAG_BLOCK_XOR[i] {
			return Err(())
		}
		// striped XOR (abababababab...)
		if input[i*2] ^ input[i*2+1] != FLAG_STRIPE_XOR[i] {
			return Err(())
		}
	}

	Ok(())
}

#[inline]
/// Checks that the FNV-1a hash of the input matches the flag's hash.
fn check_total_fnv(input: &[u8]) -> Result<(), ()> {
	// copy input into buffer with trailing zeros as padding
	let mut buf = [0; FLAG_LEN + 8];
	buf[0..FLAG_LEN].copy_from_slice(input);

	// compute FNV-1a 64-bit hash
	let mut val = FNV_1A_BASIS;

	for chunk in buf.chunks_exact(8) {
		let elem = u64::from_be_bytes(chunk.try_into().unwrap());
		val ^= elem;
		val = val.wrapping_mul(FNV_1A_PRIME);
	}

	if val == FLAG_FNV {
		Ok(())
	} else {
		Err(())
	}
}

#[inline]
/// Checks that all input characters are within a specific range.
fn check_chars(input: &[u8]) -> Result<(), ()> {
	for chr in input {
		if !(chr.is_ascii_lowercase() || chr.is_ascii_digit() || chr.is_ascii_punctuation()) {
			return Err(())
		}
	}

	Ok(())
}


/// Returns true if the given data matches the flag, false otherwise.
pub(crate) fn verify_internal(data: &[u8]) -> Result<(), ()> {
	// check length
	if data.len() != FLAG_LEN {
		return Err(())
	}

	// check flag prefix
	if !data.starts_with(b"clubeh") {
		return Err(())
	}

	check_xor_halves(data)?;

	check_total_fnv(data)?;

	check_chars(data)?;

	Ok(())
}

/// C-compatible wrapper function to check if a given string matches the flag.
#[export_name = "verify_flag"]
pub unsafe extern "C" fn verify_flag_cstr(string: *const c_char) -> bool {
	verify_internal(CStr::from_ptr(string).to_bytes()).is_ok()
}
