use std::{io, io::Write, time::Duration};

use super::constants::*;


/// Sleep for a variable length of time.
#[inline]
fn wait(length: u64) {
	std::thread::sleep(Duration::from_micros(length * 100000))
}

/// Emit a backspace character to stdout.
#[inline]
fn backspace() {
	print!("\x08");
}

/// Map a u8 to a printable ASCII character.
fn u8_to_printable(val: u8) -> u8 {
	// initial map with XOR, just for fun
	let mut display_char = val ^ 0b00110100;
	// remap to printable ASCII range
	display_char %= b'~' - b'!';
	display_char += b'!';
	display_char
}

/// Print out the embedded flag (slowly).
pub fn print_flag() {
	// iterate through the obfuscated flag values
	for (flag_idx, flag_val) in FLAG_VALUES.iter().enumerate() {
		// iterate through every possible byte value
		for chr in 0..=u8::MAX {
			// wait for a variable amount of time
			wait((chr & 0b11) as u64 + 4);
			// wait for a linearly-increasing amount of time (based on flag position)
			wait(1024 * flag_idx as u64);

			// print character (or remapped placeholder character)
			if chr.is_ascii_graphic() {
				print!("{}", chr as char);
			} else {
				print!("{}", u8_to_printable(chr) as char);
			}

			// compute intermediate comparison operands
			let v1 = flag_val ^ VAL_XOR;
			let v2 = chr.wrapping_add(VAL_ADD);

			// wait a bit and print a backspace if v1 != v2
			// for better obfuscation, this is done with inequality operators
			// different wait durations are used to prevent the compiler from unifying the separate branches
			if v1 > v2 {
				wait(5);
				backspace();
			} else if v1 < v2 {
				wait(6);
				backspace();
			} else {
				wait(7);
			}
			// flush partial line
			io::stdout().flush().expect("failed to flush stdout");
		}
	}

	// overwrite trailing character and print newline
	println!(" ");
}
