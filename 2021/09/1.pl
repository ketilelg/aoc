#!/usr/bin/perl

my @dmap;

my$w;
my$line=0;
while(<>)
{
    $w=length;
    my @lc=split//;
    for my $c (0..$#lc)
    {
	$dmap[$line][$c]=$lc[$c];
    }

    $line++;
}
$line--;
$w--;
$w--;
my $lowsum;
my @lowx,@lowy; #holder på koords til lowpoints.
my $nlow=0;
for my $y (0..$line)
{
    for my $x (0..$w)
    {
#	print "i: $x $y -$dmap[$y][$x]-\n";
	#sjekk om er lowest..:
	if ((($x == 0) || ($dmap[$y][$x] < $dmap[$y][$x-1])) &&
	    (($x == $w) || ($dmap[$y][$x] < $dmap[$y][$x+1])) &&
	    (($y == 0) || ($dmap[$y][$x] < $dmap[$y-1][$x])) &&
            (($y == $line) || ($dmap[$y][$x] < $dmap[$y+1][$x])))
	{ #lowpoint..:
	    print "low: $x $y $dmap[$y][$x]\n";
	    $lowsum+=$dmap[$y][$x]+1;
	    $lowx[$nlow]=$x;
	    $lowy[$nlow]=$y;
	    $nlow++;

#	    $bsize=basin($x,$y);
#	    print "basin: $bbsize\n";
	}
    
    }
}
print "p1: $lowsum\n";

my @basins;
my @nb=0;;

for my $i (0..$#lowx)
{
    $b=basin($lowx[$i],$lowy[$i]);
    print "blow: $x $y $b\n";
    $basins[$nb]=$b;
    $nb++;
}

@rb= sort { $b <=> $a }@basins;

$bres=$rb[0]*$rb[1]*$rb[2];

print "p2: $bres\n";





sub basin
{
    my $x=$_[0];
    my $y=$_[1];
#    print "basin $x $y ";
    #gitt et punkt (input: x,y): finn antall punkter som ikke er 9. om vi fyller alt som ikke er 9 med 9, så bubrde det funke?
    if ($dmap[$y][$x]==9)
    { #kant, eller har vært her
#	print "X\n";
	return 0;
    }
    else
    { #skal "erstatte"
	my $ret=1;
	$dmap[$y][$x]=9;
	if (($x > 0) &&  ($dmap[$y][$x-1] < 9)) {$ret+= basin($x-1,$y);}
	if (($x < $w) &&  ($dmap[$y][$x+1] < 9)) {$ret+= basin($x+1,$y);}
	if (($y > 0) &&  ($dmap[$y-1][$x] < 9)) {$ret+= basin($x,$y-1);}
	if (($y < $line) &&  ($dmap[$y+1][$x] < 9)) {$ret+= basin($x,$y+1);}
#	print "r: $ret\n";
	return $ret;
	
    }

    
}
