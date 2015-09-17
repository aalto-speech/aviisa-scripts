#!/usr/bin/perl -w
#
# Reads a list of Finnish words or morphs, one per line, in UTF-8 encoding, and
# creates a lexicon in NOWAY/Chronos format.

use strict;
use locale;
use Encode;
use POSIX;
use Getopt::Long;
use utf8;
use vars qw/$m/;

my $input_file = "-";
my $morph_model = "";
my $options_ok = GetOptions(
	"read=s" => \$input_file,
	"morph"  => \$morph_model);
if (!$options_ok) {
	die "Invalid command line options."
}

open(my $INPUT, "< $input_file") or die "Cannot open $input_file: $!";

if ($morph_model) {
	print "<w>(1.0) __\n"
}
else { 
	print "__(1.0) __\n";
}
print "_(1.0) _\n";
print "<s>(1.0)\n";
print "</s>(1.0)\n";

while (<$INPUT>) {
	chomp;
#//	continue if /[<-]/;
        next if /[<-]/;
	my $word = decode( "utf8", $_ );

	if ( $word eq '' ) {
		next;
	}

	print encode( "utf8", $word ) . "(1.0) ";

	# Convert foreign phonemes to Finnish representatives.
	$word =~ s/ch/ts/g;	
	$word =~ s/ñ/nj/g;
	$word =~ s/qu/kv/g;
	$word =~ s/q/k/g;
	$word =~ s/w/v/g;
	$word =~ s/x/ks/g;
	$word =~ s/å/o/g;
	$word =~ s/à/a/g;
	$word =~ s/é/e/g;
	$word =~ s/í/i/g;
	$word =~ s/ó/o/g;
	$word =~ s/ú/u/g;
	$word =~ s/ý/y/g;
	$word =~ s/ü/yy/g;
	$word =~ s/æ/ä/g;
	$word =~ s/ø/ö/g;
	$word =~ s/'/_/g;     # vaa'an
	#Now some sami:
	$word =~ s/a/a/g;
	$word =~ s/á/ä/g;
	$word =~ s/b/b/g;
	$word =~ s/c/ts/g;
	$word =~ s/č/C/g;
	$word =~ s/d/d/g;
	$word =~ s/đ/D/g;
	$word =~ s/e/e/g;
	$word =~ s/m/m/g;
	$word =~ s/n/n/g;
	$word =~ s/ŋ/N/g;
	$word =~ s/o/o/g;
	$word =~ s/p/p/g;
	$word =~ s/r/r/g;
	$word =~ s/s/s/g;
	$word =~ s/š/S/g;
	$word =~ s/f/f/g;
	$word =~ s/g/g/g;
	$word =~ s/h/h/g;
	$word =~ s/i/i/g;
	$word =~ s/j/j/g;
	$word =~ s/k/k/g;
	$word =~ s/l/l/g;
	$word =~ s/t/t/g;
	$word =~ s/ŧ/T/g;
	$word =~ s/u/u/g;
	$word =~ s/v/v/g;
	$word =~ s/y/y/g;
	$word =~ s/z/ts/g;
	$word =~ s/u/u/g;
	$word =~ s/v/v/g;
	$word =~ s/ž/Z/g;

	# The phoneme symbols are in ISO-8859-15.
	$word = encode( "iso-8859-15", $word );

	for ( my $pos = 0 ; $pos < length($word) ; ++$pos ) {
		my $center = substr( $word, $pos, 1 );

		my $left = '_';
		$left = substr( $word, $pos - 1, 1 ) if ( $pos > 0 );
		$left = substr( $word, $pos - 2, 1 )
		  if ( ( $left eq '_' ) && ( $pos > 1 ) );
		$left = '_' if ( $left eq '-' );

		my $right = '_';
		$right = substr( $word, $pos + 1, 1 ) if ( $pos < length($word) - 1 );
		$right = substr( $word, $pos + 2, 1 )
		  if ( ( $right eq '_' ) && ( $pos < length($word) - 2 ) );
		$right = '_' if ( $right eq '-' );
		
		if ($center eq '_') {
			print " $center";
		}
		elsif ($center eq '-') {
			print " _p";
		}
		else {
			print " $left-$center+$right";
		}
	}
	print "\n";
}
