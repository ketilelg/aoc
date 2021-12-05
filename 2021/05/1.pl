#!/usr/bin/perl


my @s;

sub sp
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
    if ($1 == $3)
    {
	if ($2 < $4)
	{
	    for $i ($2 .. $4)
	    {
		$s[$1][$i]++;
		if ($s[$1][$i] == 2)
		{
		    $ol++;
		    print "overlap! $1 $i \n";
		}
	    }
	}
	else
	{
	    for $i ($4 .. $2)
	    {
		$s[$1][$i]++;
		if ($s[$1][$i] == 2)
		{
		    $ol++;
		    print "overlap! $1 $i\n";
		}
	    }
	}
    }
    elsif ($2 == $4)
    {
	if ($1 < $3)
	{
	    for $i ($1 .. $3)
	    {
		$s[$i][$2]++;
		if ($s[$i][$2] == 2)
		{
		    $ol++;
		    print "overlap! $i $2\n";
		}
	    }
	}
	else
	{
	    for $i ($3 .. $1)
	    {
		$s[$i][$2]++;
		if ($s[$i][$2] == 2)
		{
		    $ol++;
		    print "overlap! $i $2\n";
		}
	    }
	}
    }
    else #diagonal
    {
	if ($1 < $3)
	{
	    $sx = $1;
	    $num = $3 - $1;
	}
	else
	{
	    $sx = $3;
	    $num = $1 - $3;
	}

	if ($2 < $4)
	{
	    $sy = $2;
	    for $i (0 .. $num)
	    {
		$s[$sx+$i][$sy+$i]++;
		if ($s[$sx+$i][$sy+$i] == 2)
		{
		    $ol++;
		    print "overlap! $i $2\n";
		}
	    }

	}
	else
	{
	    $sy = $4;
	}
	
    }
    
    print "\n";
    sp;
}

print "end: $ol\n";
