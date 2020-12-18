#!/usr/bin/perl


use Data::Dumper;
use strict;


my @stack;
my $nt; #number of tokens
my $pos;
my $sum;

while (<>)
{
    chomp;
    s/\(/\(\  /g;
    s/\)/\ \)/g;

    @stack = split / /;

    $nt=$#stack;
    $pos=0;
    my $res=calc(0);
    $sum+=$res;
    print "inneholder $nt elementeR: @stack = $res\n";;

}

print "end: $sum\n";

sub calc
{
#    my $pos = $_[0];
    

    my $res=0;
    my $oper="+";
 #   print "\nc: ";
    for my $i  ($pos..$nt)
    {
	my $t=$stack[$pos];
	if ($t =~ /\d+/)
	{
#	    print " tall: $t";
	    $res = eval("$res $oper $t");
#	    print " r:$res ";
	}
	elsif ($t=~/\(/)
	{
#	    print " vp ";
	    $pos++;
	    $res = eval("$res $oper calc($pos+1)");
	}
	elsif ($t=~/\)/)
	{
#	    print " hp $res\n";

	    return $res;
	}
	elsif ($t=~/[\+\*]/)
	{
#	    print " op:$t ";
	    $oper=$t;
	}
	$pos++
    }
#    print "end c: $res\n";
    return $res;
    
}
