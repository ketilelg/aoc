#!/opt/local/bin/perl

use Quantum::Superpositions;

$/="";

while(<>)
{
my @answers = split /\W/;

my $common= In_Common(@answers);

print "common: $common\n";
s/\W//g;
my @chars = split //, $common;  

my %uniq; 
@uniq{@chars} = ();          

my $count = scalar keys %uniq;

print "linje: $_, unike: $count\n";

$total+=$count;
}
print "totalt: $total\n";

sub In_Common {
    return join '', 
        eigenstates(
            all(
                map { any( split( //, $_ ) ) } @_
            )
        );
}
