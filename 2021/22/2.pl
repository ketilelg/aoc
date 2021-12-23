#!/usr/bin/perl

use strict;
use warnings;
use Data::Dump;
use List::Util qw(min max);

my @core; #array of arry, alle cuboids
my $nc=0; #number of active cores

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

my @isret; #return from intersect, om det er noe..

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
    my $ton=$_[12];
    if ((($x11 <= $x22) && ($x12 >= $x21)) &&
	(($y11 <= $y22) && ($y12 >= $y21)) &&
	(($z11 <= $z22) && ($z12 >= $z21)))
    {
	#finn overlappregionen..
	my $nx1=max($x11,$x21);
	my $nx2=min($x12,$x22);
	my $ny1=max($y11,$y21);
	my $ny2=min($y12,$y22);
	my $nz1=max($z11,$z21);
	my $nz2=min($z12,$z22);
	@isret = ("over",$nx1,$nx2,$ny1,$ny2,$nz1,$nz2);	
	my $vol=($nx2-$nx1+1)*($ny2-$ny1+1)*($nz2-$nz1+1);
	print "overlap, $nx1, $nx2, $ny1, $ny2, $nz1, $nz2 = $vol \n";
	return $vol;
    }
    return 0;
}


my $tv=0;

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
    my @nc= ([$1,$2,$3,$4,$5,$6,$7]);

    my $lv=$w*$h*$d;

    for my $co (@core)
    {
	my $isect=intersect($2,$3,$4,$5,$6,$7,$co->[1],
			  $co->[2],$co->[3],$co->[4],$co->[5],$co->[6],$ton);
	if ($isect>0)
	{ #vi intersecter med noe gammelt..:
	    if($ton) #er denne en on-kommando? 
	    {
		$tv+=$lv;
		#intersectet vi med en gammel on?
		if($co->[0] eq "on")
		{
		    print "is1 $tv\n";
		    push @core, [@isret];
		    dd \@isret;
		    $tv= $tv-(($isret[2]-$isret[1]+1)*($isret[4]-$isret[3]+1)*($isret[6]-$isret[5]+1));
		}
		elsif($co->[0] eq "over")
		{
		    print "is2 $tv\n";
		}
		else
		{
		    print "is3 $tv\n";
		}
	    }
	    else #off-kommando
	    {
		if($co->[0] eq "on")
		{
		    print "is4 $tv\n";
		}
		elsif($co->[0] eq "over")
		{
		    print "is5 $tv\n";
		}
		else
		{
		    print "is6 $tv\n";
		}
	    }
	}
    }

    push @core, @nc;
    
}

dd \@core;
