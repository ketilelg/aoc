#!/usr/bin/perl

my %pm = ( '(' => ')',
	   ')' => '(',
	   '<' => '>',
	   '>' => '<',
	   '[' => ']',
	   ']' => '[',
	   '{' => '}',
	   '}' => '{' );

my %points = ( ')' => 3,
	       ']' => 57,
	       '}' => 1197,
	       '>' => 25137 );

my %cpoints = ( '(' => 1,
		'[' => 2,
		'{' => 3,
		'<' => 4 );


my $err=0;
my $p2p=0; #part 2 points
my @p2t;
my $p2c=0;

while(<>)
{
    chomp;
#    print "ytre, linja: -$_-\n";
    $p2p=parse($_);

    if ($p2p>0)
    {
	$p2t[$p2c]=$p2p;
	$p2c++;
    }
    
    print "del2: $p2p\n";
}
    print "del1: $err\n";

my @sortp2= sort { $a <=> $b } @p2t;

print "p2: \n @p2t \n @sortp2 \n $sortp2[($p2c-1)/2]\n";

sub parse
{
    my $str=$_[0];
    my @stack;
    my $level=0;
    foreach $c (split //, $str)
    {
	if ($c =~ /(^[\<\[\(\{])/)
	{
	    $stack[$level]=$c;
	    $level++;
	}
	else
	{
	    $level--;
	    my $ll=$pm{$c};
	    if ($ll eq $stack[$level])
	    {
	    }
	    else
	    {
		$err+=$points{$c};
		return;
	    }

	}
	    
    }

    my $pp=0;
    while ($level>0)
    {
	$level--;
	$pp*=5;
	$pp+=$cpoints{$stack[$level]};
    }
    return $pp;
}

