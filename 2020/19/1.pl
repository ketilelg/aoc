#!/usr/bin/perl

my @rules;
my %legal;


# les regler:
my $done=0;
my $firstrule=0;
my $finalrule;
while(!$done)
{
    $_=<>;
    chomp;
#    print $_;

    if (/(\d+)\:\s\"?([ab\|\d\s]+)\"?/)
    {
	print " 1- $1: 2-$2\n";
	$rules[$1]=" $2 ";
#	if ($firstrule<0){$firstrule=$1;}
    }
    else
    {
	$done=1; #blank linje
    }
}

#process rules into %allowed:

procrules(0);

print "finalrule: -$finalrule-\n";

my $num;
while(<>)
{
    chomp;


    $term=$_;
#        print "-$term- $finalrule\n";
    if ($finalrule=~/$term/)
    {
	print "$_ legal \n";
	$num++;
    }

}

print "part1: $num\n\n";

sub procrules
{
    #tar ruleno, rulestr som input..?
    my $r=$_[0];
    my $changed=0;
    my $scd=0;

 
    do
    {
	$sc=0;
	
    do
    {
	$changed=0;
	print "doloop\n";
	
    for my $i (0..$#rules)
    {
	    #er denne reglen med i noen andre, og er den en splittregel?
    if($rules[$i]=~/(.+?)\|(.+)/)
    { #er splittregel..:
	my $a=$1;
	my $b=$2;
	print "spli $i $a-$b\n";

	for $j (0..$#rules)
	{ # om regel i er med i andre, iterer over j: anvend.. 
	    print "c: $i $j : .$rules[$j].\n";
	    if($rules[$j]=~/(.+?\s)$i(\s.+)/)
	    {
		print "$i is in: .$1. -- .$2. .$a. .$b.r: $rules[$j]\n";
		my $c=$1;
		my $d=$2;

		$changed+=$rules[$j]=~s/([^\|]*)\s$i\s([^\|]*)/$1$a$2\ \|$1$b$2/g;
		$sc=$changed;
		print "ce:      $rules[$j]\n\n";
	    }

	}
    }
    }
    } until (!$changed);

    print "done split\n";

   do
    { # ekspander talla
        $changed=0;
	print "2doloop\n";
	
	for my $i (0..$#rules)
	{
	if(!($rules[$i]=~/[ab]/))
	{
   
	print "repl $i\n";

	for $j (0..$#rules)
	{ # om regel i er med i andre, iterer over j: anvend.. 
	    print "rc: $i $j : .$rules[$j].\n";
	    if($rules[$j]=~/(.*\s)$i(\s.*)/)
	    {
		print "r $i is in: .$1. -- .$2. r: $rules[$j]\n";
		my $c=$1;
		my $d=$2;

		$changed+=$rules[$j]=~s/\s$i\s/ $rules[$i] /g;
		$sc+=$changed;
		print "rce:      $rules[$j]\n\n";
	    }

	}
	}
	}
    } until (!$changed);

    
    print "done numerics\n";

    } until (!$sc);

    # swap in a&b

    $finalrule=$rules[$firstrule];

    for my $i (0..$#rules)
    {
	if($rules[$i]=~/([ab])/)
	{
	    $l=$1;
	    print "bb: $l $finalrule\n";
	    $finalrule=~s/$i/$l/g;
	    print "bc: $finalrule\n";
	}
    }
    #strip to compact string:
    $finalrule="|".$finalrule."|";
    $finalrule=~s/\s?//g;
    print "final: $finalrule\n";
    
}

sub xprocrules
{
    #tar ruleno, rulestr som input..?
    my $r=$_[0];
    my $changed=0;
    do
    {
	$changed=0;
    for my $i (0..$#rules)
    {
	print "\nr:.$rules[$i].\n";
	if (!($rules[$i]=~/[\d\|]/))
	{ 
	    # kan kun inneholde bokstav(er)
	    for my $j (0..$#rules)
	    {
		print "$i $j. ja\n";
		if($rules[$j]=~s/$i/$rules[$i]/g)	{	$changed++; }
	    }
	}
	elsif ($rules[$i]=~/([ab])\s([ab])\s\|\s([ab])\s([ab])/)
	{
		my $a=$1;
		my $b=$2;
		my $c=$3;
		my $d=$4;
	    for my $j (0..$#rules)
	    {
		print "$i $j. -$1-$2-$3-$4-jah\n";
		if ($rules[$j]=~s/$i/$a$b\|$c$d/g) {		$changed++;}
	    }
	    
	}
	elsif ($rules=~/[ab]/)
	{
	}
	printrules();
    }
    }
    until (!$changed);
}

sub printrules
{
    for my $i (0..$#rules)
    {
	print "$i: .$rules[$i].\n";
    }

}
