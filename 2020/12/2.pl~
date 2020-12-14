#!/opt/local/bin/perl
use Switch;
use Math::Trig;
my $npos=0;
my $epos=0;
my $dir=90; #facing east. 0=north, -90=west, 180=south


while(<>)
{
    chomp;
    print $_;

    /(\w)(\d+)/;

    switch($1) {
	case "N" { $npos+=$2; }
	case "S" { $npos-=$2; }
	case "E" { $epos+=$2; }
	case "W" { $epos-=$2; }
	case "L" { $dir-=$2; }
	case "R" { $dir+=$2; }
	case "F" { $npos+=cos(deg2rad($dir)) * $2; $epos+=sin(deg2rad($dir))*$2; }
    }
    print " $1: n: $npos e: $epos dir: $dir\n";
}
