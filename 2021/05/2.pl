#!/usr/bin/perl


my @s;

sub sp #print (small) map
{
    for $y (0..9)
    {
	for $x (0..9)
	{
	    if ($s[$x][$y] > 0)
	    {
		print $s[$x][$y];
	    }
	    else
	    {
		print ".";
	    }
	}
	print "\n";
    }
}


while (<>)
{
    /(\d+),(\d+) -> (\d+),(\d+)/;
    print "linje: $1 $2 $3 $4\n";

    $lx=abs($1-$3); #avstand i x
    if ($1 != $3)
    {
	$dx = $lx/($3-$1);
    }
    else
    {
	$dx=0;
    } #retning i x

    $ly=abs($2-$4); #avstand i y

    if ($2 != $4)
    {
	$dy = $ly/($4-$2);
    } else
    {
	$dy =0;
    } #retning i y
    
    if ($lx>$ly) {$steps=$lx;} else {$steps=$ly;}

    print "$lx $dx $ly $du $steps\n";
    
    for $i (0 .. $steps)
	    {
		$s[$1+($i*$dx)][$2+($i*$dy)]++;
		if ($s[$1+($i*$dx)][$2+($i*$dy)] == 2)
		{
		    $ol++;
		    print "overlap! $1 $i \n";
		}
	    }
	
    
    
#    print "\n";
#    sp;
}

print "end: $ol\n";
