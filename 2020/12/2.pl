#!/opt/local/bin/perl
use Switch;
use Math::Trig;
my $npos=1;
my $epos=10; #waypoint pos
my $spn=0;
my $spe=0; #ships pos
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
	case "L" { myrot(360-$2);}
	case "R" { myrot($2); }
	case "F" { $spn+=$2*$npos; $spe+=$2*$epos; }
    }
    $dir=($dir+360) % 360;
    print " $1: n: $npos e: $epos spn: $spn spe: $spe\n";
}

sub myrot {
switch ($_[0]) {
    case 90 { my $w=$npos; $npos= -$epos; $epos=$w; }
    case 180 { $npos= -$npos; $epos= -$epos; }
    case 270 { my $w=$npos; $npos= $epos; $epos=-$w; }
}
}
