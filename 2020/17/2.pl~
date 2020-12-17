#!/usr/bin/perl


use Storable qw(dclone);
use Data::Dumper;
use strict;

my $offset=10;

my @pdim;
my @newpdim;

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
	$pdim[$z][$y+$height][$x+$width] = $c;
	$width++;
    }

    
    $height++;
}

# $height--;
# $width--;


print "d: $depth h: $height w: $width\n";

#print Dumper(@pdim);

# printit();
# my $change=1;
my $numc=0;
for my $i (1..6)
{
print "x: $x y: $y z: $z d: $depth h: $height w: $width\n";

    printit();
    $numc=0;
    for my $zc ($z-1..$z+$depth) {
	for my  $yc  ($y-1..$y+$height) {
	    for my $xc ($x-1..$x+$width)  {

		my $neigh=numocc($zc,$yc,$xc);
#				print "\nw: $zc $yc $xc $neigh\n\n";

		if ($pdim[$zc][$yc][$xc] eq "#")
		{
		    if (($neigh==2)||($neigh==3))
		    {
			$newpdim[$zc][$yc][$xc] = "#";
			$numc++;
		    }
		    else
		    {
			$newpdim[$zc][$yc][$xc] = ".";
		    }
		}
		else #enten . eller undefined. vi bryr oss ikke
		{
		    if (($neigh==3))
		    {
			$newpdim[$zc][$yc][$xc] = "#";
			$numc++
		    }
		    else
		    {
			$newpdim[$zc][$yc][$xc] = ".";
		    }
		}
	    }
	}
    }

#    print Dumper(@pdim);

    $y--;
    $x--;
    $z--;
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
# returnerer antall naboer (i 3 dimensjoner) som er aktive, gitt z,y,x som input.
{
    my $zp=$_[0];
    my $yp=$_[1];
    my $xp=$_[2];
    my $num=0;

    for my $sx ($xp-1..$xp+1)
    {
	for my $sy ($yp-1..$yp+1)
	{
	    for my $sz ($zp-1..$zp+1)
	    {
		if (!(($sx==$xp)&&($sy==$yp)&&($sz==$zp))&&($pdim[$sz][$sy][$sx] eq "#"))
		{
		    $num++;
		}
	    }
	}
    }
    return $num;
}

