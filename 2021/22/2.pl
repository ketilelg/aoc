#!/usr/bin/perl

use List::Util qw(min max);

my @core; #array of arry, alle cuboids
#
#

sub isinter
    # ER to kuboider overlappende? tar x1,x2,y1,y2,z1,z2,X1,X2,Y1,Y2,Z1,Z2
    # som input. returnerer 1 om de overlapper. 
{
    my $x11=$_[0];
    my $x12=$_[1];
    my $y11=$_[2];
    my $y12=$_[3];
    my $z11=$_[4];
    my $z12=$_[5];
    my $x21=$_[6];
    my $x22=$_[7];
    my $y21=$_[8];
    my $y22=$_[9];
    my $z21=$_[10];
    my $z22=$_[11];
    if ((($x11 <= $x22) && ($x12 >= $x21)) &&
	(($y11 <= $y22) && ($y12 >= $y21)) &&
	(($z11 <= $z22) && ($z12 >= $z21)))
    {
	return 1;
    }
    return 0;
}

sub intersect
    #
    # gitt to kuboider, finn intersection
{
    my $x11=$_[0];
    my $x12=$_[1];
    my $y11=$_[2];
    my $y12=$_[3];
    my $z11=$_[4];
    my $z12=$_[5];
    my $x21=$_[6];
    my $x22=$_[7];
    my $y21=$_[8];
    my $y22=$_[9];
    my $z21=$_[10];
    my $z22=$_[11];
    if ((($x11 <= $x22) && ($x12 >= $x21)) &&
	(($y11 <= $y22) && ($y12 >= $y21)) &&
	(($z11 <= $z22) && ($z12 >= $z21)))
    {
	#finn overlappregionen..
    }
    return 0;
}

my @nc=0;

while(<>)
{
    /(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)/;

    my $w=$3-$2+1;
    my $h=$5-$4+1;
    my $d=$7-$6+1;
    my $ton = 0;
    if ($1 eq "on")
    {
	$ton=1;
    }
    print "k: $1,$2,$3,$4,$5,$6,$7 $w x $h x $d\n";

}


