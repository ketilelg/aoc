#!/usr/bin/perl


use Storable qw(dclone);
use Data::Dumper;
use strict;

my $offset=10;

my @pdim;
my @newpdim;

my $w=$offset;
my $length=1;
my $x=$offset;
my $width;
my $y=$offset;
my $height;
my $z=$offset;
my $depth=1;

while (<>)
{
    chomp;
    $width=0;
    for my $c  (split //)
    {
	$pdim[$w][$z][$y+$height][$x+$width] = $c;
	$width++;
    }

    
    $height++;
}

# $height--;
# $width--;



#print Dumper(@pdim);

# printit();
# my $change=1;
my $numc=0;
for my $i (1..6)
{
print "x: $x y: $y z: $z w: $w d: $depth h: $height w: $width l:$length\n";

    printit();
    $numc=0;

for my $wc ($w-1..$z+$length) {
    for my $zc ($z-1..$z+$depth) {
	for my  $yc  ($y-1..$y+$height) {
	    for my $xc ($x-1..$x+$width)  {

		my $neigh=numocc($wc,$zc,$yc,$xc);
#				print "\nw: $zc $yc $xc $neigh\n\n";

		if ($pdim[$wc][$zc][$yc][$xc] eq "#")
		{
		    if (($neigh==2)||($neigh==3))
		    {
			$newpdim[$wc][$zc][$yc][$xc] = "#";
			$numc++;
		    }
		    else
		    {
			$newpdim[$wc][$zc][$yc][$xc] = ".";
		    }
		}
		else #enten . eller undefined. vi bryr oss ikke
		{
		    if (($neigh==3))
		    {
			$newpdim[$wc][$zc][$yc][$xc] = "#";
			$numc++
		    }
		    else
		    {
			$newpdim[$wc][$zc][$yc][$xc] = ".";
		    }
		}
	    }
	}
    }

    #    print Dumper(@pdim);
}

    $y--;
    $x--;
    $z--;
    $w--;
    $length+=2;
    $height+=2;
    $width+=2;
    $depth+=2;
    # kopier newpdim til pdim.
    @pdim = @{ dclone(\@newpdim)};
    print "endloop: numc= $numc\n";
}


sub printit
    # skriver ut @pdim
{
    for my $zc ($z-1..$z+$depth) {
	print "z: $zc\n";
	for my  $yc  ($y-1..$y+$height) {
	    for my $xc ($x-1..$x+$width) 
		{
		    if ($pdim[$zc][$yc][$xc] eq "#") {print "#";}
		    elsif ($pdim[$zc][$yc][$xc] eq ".") {print ".";}
		    else {print " ";}
		}
	    print " $yc\n"
	}
	print "\n";
	
    }
    
}


sub numocc
# returnerer antall naboer (i 3 dimensjoner) som er aktive, gitt w,z,y,x som input.
{
    my $wp=$_[0];
    my $zp=$_[1];
    my $yp=$_[2];
    my $xp=$_[3];
    my $num=0;

    for my $sx ($xp-1..$xp+1)
    {
	for my $sy ($yp-1..$yp+1)
	{
	    for my $sz ($zp-1..$zp+1)
	    {
		for my $sw ($wp-1..$wp+1)
		{
		    if (!(($sx==$xp)&&($sy==$yp)&&($sz==$zp)&&($sw==$wp))&&($pdim[$sw][$sz][$sy][$sx] eq "#"))
		    {
			$num++;
		    }
		}
	    }
	}
    }
    return $num;
}

