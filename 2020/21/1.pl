#!/opt/local/bin/perl

use strict;

use Set::Scalar;

# $s = Set::Scalar->new;
# $s->insert('a', 'b');
# $s->delete('b');
# $t = Set::Scalar->new('x', 'y', $z);

my %ings;
my %als; 
my %numocc;

while(<>)
{
    chomp;
    /(.+)\(contains\s(.+)\)/;
    
    my @inp = split(" ",$1);

    my @algs= split(", ",$2);

    for my $i (0..$#algs)
    {
	if($als{$algs[$i]})
	{ #det er noe der
	    print "E";
	    my $t=Set::Scalar->new(@inp);
	    $als{$algs[$i]} = $als{$algs[$i]}->intersection($t);
	    print " $als{$inp[$i]} ";
	}
	else
	{ #fantes ikke. bare putt inn.
	    print "N";
	    $als{$algs[$i]}= Set::Scalar->new(@inp);
	}

    }
    
    
    for my $i (0..$#inp)
    {
	print "$inp[$i]: ";
	$numocc{$inp[$i]}++;
	if (scalar @algs > 0)
	{
	    if($ings{$inp[$i]})
	    { #det finnes noe der..
 		print "E";
		my $t=Set::Scalar->new(@algs);
		$ings{$inp[$i]} = $ings{$inp[$i]}->intersection($t);
		print " $ings{$inp[$i]} ";
	    }
	    else
	    { #fantes ikke. bare putt inn.
		print "N";
		$ings{$inp[$i]}= Set::Scalar->new(@algs);
	    }
	    
		for my $j (0..$#algs)
		{
		    print "-$algs[$j]- ";
		}
		print "\n";
	}
    }
    print "----\n";
}

foreach my $k (keys %ings)
{
    print "$numocc{$k} $k : $ings{$k}\n";
}

foreach my $k (keys %als)
{
    print "a: $k : $als{$k}\n";
}

